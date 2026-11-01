import json
from datetime import datetime
from typing import Any, Dict, List


class Produto:
    def __init__(self, nome: str, preco: float, criado_em: datetime) -> None:
        self.nome = nome
        self.preco = preco
        self.criado_em = criado_em

    def __repr__(self) -> str:
        return f"Produto(nome={self.nome!r}, preco={self.preco}, criado_em={self.criado_em.isoformat()})"


def produto_para_dict(produto: "Produto") -> Dict[str, Any]:
    """Converte um Produto em dicionário serializável.

    Args:
        produto (Produto): Produto a converter.

    Returns:
        dict: Dicionário com criado_em em formato ISO.

    Example:
        >>> produto_para_dict(Produto("A", 1.0, datetime(2025, 1, 1)))["criado_em"]
        '2025-01-01T00:00:00'
    """
    return {
        "nome": produto.nome,
        "preco": produto.preco,
        "criado_em": produto.criado_em.isoformat(),
    }


def dict_para_produto(dados: Dict[str, Any]) -> "Produto":
    """Converte um dicionário em Produto.

    Args:
        dados (dict): Dicionário com nome, preco e criado_em (ISO).

    Returns:
        Produto: Objeto reconstruído.

    Example:
        >>> dict_para_produto({"nome": "A", "preco": 1.0, "criado_em": "2025-01-01T00:00:00"}).nome
        'A'
    """
    return Produto(dados["nome"], dados["preco"], datetime.fromisoformat(dados["criado_em"]))


produtos: List[Produto] = [
    Produto("Notebook", 3200.00, datetime(2025, 1, 10, 9, 30)),
    Produto("Mouse", 89.90, datetime(2025, 2, 5, 14, 0)),
    Produto("Monitor", 1200.00, datetime(2025, 3, 20, 11, 15)),
]

json_str = json.dumps([produto_para_dict(p) for p in produtos], indent=2, ensure_ascii=False)
print(json_str)

recuperados = [dict_para_produto(d) for d in json.loads(json_str)]
print()
for p in recuperados:
    print(p)