from typing import Any, Dict, Optional, Union


def buscar_usuario(id: int, nome: Union[str, None]) -> Optional[Dict[str, Any]]:
    """Busca os dados de um usuário a partir do id e do nome.

    Args:
        id (int): Identificador do usuário. Deve ser não negativo.
        nome (Union[str, None]): Nome do usuário ou None se desconhecido.

    Returns:
        Optional[Dict[str, Any]]: Dicionário com os dados do usuário, ou
        None se o id for negativo.

    Example:
        >>> buscar_usuario(1, "Ana")
        {'id': 1, 'nome': 'Ana', 'ativo': True}
        >>> buscar_usuario(-5, "Ana") is None
        True
    """
    if id < 0:
        return None
    return {"id": id, "nome": nome if nome is not None else "Desconhecido", "ativo": True}


print(buscar_usuario(1, "Ana"))
print(buscar_usuario(2, None))
print(buscar_usuario(-1, "Carlos"))