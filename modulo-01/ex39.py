import json
import re
from typing import Dict, List


def carregar_dados(caminho: str) -> List[dict]:
    """Carrega os dados brutos de um arquivo JSON.

    Args:
        caminho (str): Caminho do arquivo JSON.

    Returns:
        list[dict]: Lista de registros.

    Example:
        >>> carregar_dados("clientes_brutos.json")[0]["id"]
        1
    """
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)


def normalizar_dados(dados: List[dict]) -> List[dict]:
    """Limpa nomes, e-mails e telefones.

    Args:
        dados (list[dict]): Registros brutos.

    Returns:
        list[dict]: Registros com nome capitalizado, e-mail em minúsculas
        e telefone somente com dígitos.

    Example:
        >>> normalizar_dados([{"id": 1, "nome": "  jOÃO   silva ", "email": "A@B.COM", "telefone": "(11) 91234-5678"}])[0]["nome"]
        'João Silva'
    """
    resultado = []
    for c in dados:
        nome = " ".join(c["nome"].split()).title()
        resultado.append({
            "id": c["id"],
            "nome": nome,
            "email": c["email"].strip().lower(),
            "telefone": re.sub(r"\D", "", c["telefone"]),
        })
    return resultado


def enriquecer_dados(dados: List[dict]) -> List[dict]:
    """Adiciona campos derivados aos registros.

    Args:
        dados (list[dict]): Registros normalizados.

    Returns:
        list[dict]: Registros com telefone_formatado, dominio_email e iniciais.

    Example:
        >>> enriquecer_dados([{"id": 1, "nome": "Ana Lima", "email": "a@b.com", "telefone": "11912345678"}])[0]["iniciais"]
        'AL'
    """
    resultado = []
    for c in dados:
        tel = c["telefone"]
        formatado = f"({tel[:2]}) {tel[2:7]}-{tel[7:]}" if len(tel) == 11 else tel
        resultado.append({
            **c,
            "telefone_formatado": formatado,
            "dominio_email": c["email"].split("@")[-1],
            "iniciais": "".join(p[0] for p in c["nome"].split()),
        })
    return resultado


def exportar_resultado(dados: List[dict], caminho: str) -> None:
    """Exporta os dados tratados para um arquivo JSON.

    Args:
        dados (list[dict]): Registros tratados.
        caminho (str): Caminho do arquivo de saída.

    Returns:
        None

    Example:
        >>> exportar_resultado([], "saida.json")
    """
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)


brutos = [
    {"id": 1, "nome": "  mARIA   das  graças ", "email": " MARIA@EMAIL.COM ", "telefone": "11987654321"},
    {"id": 2, "nome": "JOÃO pedro", "email": "JOAO.PEDRO@GMAIL.COM", "telefone": "21 91234 5678"},
    {"id": 3, "nome": "ana   CLARA souza", "email": "ANA@EMPRESA.COM.BR", "telefone": "(31)99876-5432"},
    {"id": 4, "nome": "  carlos  EDUARDO ", "email": "CARLOS@OUTLOOK.COM", "telefone": "41988887777"},
    {"id": 5, "nome": "fernanda LIMA", "email": "FERNANDA@YAHOO.COM", "telefone": "51-97777-6666"},
]

with open("clientes_brutos.json", "w", encoding="utf-8") as f:
    json.dump(brutos, f, indent=2, ensure_ascii=False)

dados = carregar_dados("clientes_brutos.json")
dados = normalizar_dados(dados)
dados = enriquecer_dados(dados)
exportar_resultado(dados, "clientes_tratados.json")

print(json.dumps(carregar_dados("clientes_tratados.json"), indent=2, ensure_ascii=False))