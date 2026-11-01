import json
import os
from typing import Optional

ARQUIVO_ALUNOS = "alunos.json"
ARQUIVO_RELATORIO = "relatorio_turma.json"


def _media_aluno(aluno: dict) -> float:
    notas = aluno["notas"]
    return sum(notas) / len(notas) if notas else 0.0


def _salvar_alunos(alunos: list[dict]) -> None:
    with open(ARQUIVO_ALUNOS, "w", encoding="utf-8") as f:
        json.dump(alunos, f, indent=2, ensure_ascii=False)


def listar_alunos() -> list[dict]:
    """Lista todos os alunos cadastrados.

    Returns:
        list[dict]: Lista de alunos, vazia se não houver arquivo.

    Example:
        >>> listar_alunos()
        []
    """
    if not os.path.exists(ARQUIVO_ALUNOS):
        return []
    with open(ARQUIVO_ALUNOS, "r", encoding="utf-8") as f:
        return json.load(f)


def cadastrar_aluno(nome: str, email: str, idade: int, notas: list[float]) -> dict:
    """Cadastra um novo aluno e persiste em alunos.json.

    Args:
        nome (str): Nome do aluno.
        email (str): E-mail do aluno.
        idade (int): Idade do aluno.
        notas (list[float]): Notas do aluno.

    Returns:
        dict: Registro do aluno cadastrado.

    Example:
        >>> cadastrar_aluno("Ana", "ana@email.com", 20, [8.0, 9.0])["id"]
        1
    """
    alunos = listar_alunos()
    novo_id = max((a["id"] for a in alunos), default=0) + 1
    aluno = {
        "id": novo_id,
        "nome": nome,
        "email": email,
        "idade": idade,
        "notas": notas,
        "ativo": True,
    }
    alunos.append(aluno)
    _salvar_alunos(alunos)
    return aluno


def buscar_por_nome(nome: str) -> Optional[dict]:
    """Busca um aluno pelo nome, sem diferenciar maiúsculas de minúsculas.

    Args:
        nome (str): Nome do aluno.

    Returns:
        dict | None: Aluno encontrado ou None.

    Example:
        >>> buscar_por_nome("inexistente") is None
        True
    """
    for aluno in listar_alunos():
        if aluno["nome"].lower() == nome.lower():
            return aluno
    return None


def calcular_media_turma() -> float:
    """Calcula a média geral da turma (média das médias dos alunos).

    Returns:
        float: Média da turma, ou 0.0 se não houver alunos.

    Example:
        >>> calcular_media_turma()
        0.0
    """
    alunos = listar_alunos()
    if not alunos:
        return 0.0
    return sum(_media_aluno(a) for a in alunos) / len(alunos)


def exportar_relatorio() -> None:
    """Gera relatorio_turma.json com o resumo da turma.

    O relatório contém total de alunos, média geral, aluno com maior
    média e aluno com menor média.

    Returns:
        None

    Example:
        >>> exportar_relatorio()
    """
    alunos = listar_alunos()
    if not alunos:
        relatorio = {
            "total_alunos": 0,
            "media_geral": 0.0,
            "maior_media": None,
            "menor_media": None,
        }
    else:
        melhor = max(alunos, key=_media_aluno)
        pior = min(alunos, key=_media_aluno)
        relatorio = {
            "total_alunos": len(alunos),
            "media_geral": round(calcular_media_turma(), 2),
            "maior_media": {"nome": melhor["nome"], "media": round(_media_aluno(melhor), 2)},
            "menor_media": {"nome": pior["nome"], "media": round(_media_aluno(pior), 2)},
        }
    with open(ARQUIVO_RELATORIO, "w", encoding="utf-8") as f:
        json.dump(relatorio, f, indent=2, ensure_ascii=False)


for arq in (ARQUIVO_ALUNOS, ARQUIVO_RELATORIO):
    if os.path.exists(arq):
        os.remove(arq)

cadastrar_aluno("Ana Souza", "ana@email.com", 20, [9.0, 8.5, 9.5])
cadastrar_aluno("Bruno Lima", "bruno@email.com", 22, [7.0, 6.5, 8.0])
cadastrar_aluno("Carla Dias", "carla@email.com", 19, [10.0, 9.5, 9.0])
cadastrar_aluno("Diego Alves", "diego@email.com", 24, [5.5, 6.0, 7.0])

print("=== Alunos cadastrados ===")
for a in listar_alunos():
    print(f"{a['id']} | {a['nome']:<12} | {a['email']:<18} | {a['idade']} anos | notas: {a['notas']}")

print("\n=== Busca ===")
print(buscar_por_nome("carla dias"))

print("\n=== Média da turma ===")
print(f"{calcular_media_turma():.2f}")

exportar_relatorio()
print("\n=== Relatório exportado ===")
with open(ARQUIVO_RELATORIO, "r", encoding="utf-8") as f:
    print(json.dumps(json.load(f), indent=2, ensure_ascii=False))