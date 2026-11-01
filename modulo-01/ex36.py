import json
import os
from typing import Dict, List, Optional

ARQUIVO = "contatos.json"


def _salvar(contatos: List[Dict[str, str]]) -> None:
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(contatos, f, indent=2, ensure_ascii=False)


def listar_contatos() -> List[Dict[str, str]]:
    """Lista todos os contatos da agenda.

    Returns:
        list: Lista de contatos, vazia se não houver arquivo.

    Example:
        >>> listar_contatos()
        []
    """
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def adicionar_contato(nome: str, telefone: str, email: str) -> None:
    """Adiciona um contato à agenda.

    Args:
        nome (str): Nome do contato.
        telefone (str): Telefone do contato.
        email (str): E-mail do contato.

    Returns:
        None

    Example:
        >>> adicionar_contato("Ana", "11999990000", "ana@email.com")
    """
    contatos = listar_contatos()
    contatos.append({"nome": nome, "telefone": telefone, "email": email})
    _salvar(contatos)


def buscar_contato(nome: str) -> Optional[Dict[str, str]]:
    """Busca um contato pelo nome, sem diferenciar maiúsculas de minúsculas.

    Args:
        nome (str): Nome do contato.

    Returns:
        dict | None: Contato encontrado ou None.

    Example:
        >>> buscar_contato("inexistente") is None
        True
    """
    for contato in listar_contatos():
        if contato["nome"].lower() == nome.lower():
            return contato
    return None


def remover_contato(nome: str) -> bool:
    """Remove um contato pelo nome.

    Args:
        nome (str): Nome do contato.

    Returns:
        bool: True se removido, False se não encontrado.

    Example:
        >>> remover_contato("inexistente")
        False
    """
    contatos = listar_contatos()
    restantes = [c for c in contatos if c["nome"].lower() != nome.lower()]
    if len(restantes) == len(contatos):
        return False
    _salvar(restantes)
    return True


if os.path.exists(ARQUIVO):
    os.remove(ARQUIVO)

adicionar_contato("Ana Souza", "11999990001", "ana@email.com")
adicionar_contato("Bruno Lima", "21999990002", "bruno@email.com")
adicionar_contato("Carla Dias", "31999990003", "carla@email.com")

print("Contatos:")
for c in listar_contatos():
    print(f"  {c['nome']} | {c['telefone']} | {c['email']}")

print("\nBusca por 'bruno lima':", buscar_contato("bruno lima"))
print("Removendo 'Ana Souza':", remover_contato("Ana Souza"))
print("Removendo 'Fulano':", remover_contato("Fulano"))

print("\nContatos após remoção:")
for c in listar_contatos():
    print(f"  {c['nome']} | {c['telefone']} | {c['email']}")