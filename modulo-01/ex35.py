import json
from typing import Any, Dict, List

vendas_json = """
[
    {"mes": "Janeiro",  "produto": "Notebook", "quantidade": 45, "valor_unit": 3200.00},
    {"mes": "Janeiro",  "produto": "Mouse",    "quantidade": 120, "valor_unit": 89.90},
    {"mes": "Fevereiro","produto": "Notebook", "quantidade": 38, "valor_unit": 3200.00},
    {"mes": "Fevereiro","produto": "Teclado",  "quantidade": 75, "valor_unit": 149.90},
    {"mes": "Março",    "produto": "Monitor",  "quantidade": 30, "valor_unit": 1200.00},
    {"mes": "Março",    "produto": "Mouse",    "quantidade": 200,"valor_unit": 89.90}
]
"""


def calcular_total_mes(vendas: List[Dict[str, Any]], mes: str) -> float:
    """Calcula a receita total de um mês.

    Args:
        vendas (list): Lista de vendas.
        mes (str): Nome do mês.

    Returns:
        float: Receita total do mês.

    Example:
        >>> calcular_total_mes([{"mes": "Janeiro", "quantidade": 2, "valor_unit": 10.0}], "Janeiro")
        20.0
    """
    return sum(v["quantidade"] * v["valor_unit"] for v in vendas if v["mes"] == mes)


def produto_mais_vendido(vendas: List[Dict[str, Any]]) -> str:
    """Retorna o produto com maior quantidade total vendida.

    Args:
        vendas (list): Lista de vendas.

    Returns:
        str: Nome do produto mais vendido.

    Example:
        >>> produto_mais_vendido([{"produto": "A", "quantidade": 1}, {"produto": "B", "quantidade": 5}])
        'B'
    """
    totais: Dict[str, int] = {}
    for v in vendas:
        totais[v["produto"]] = totais.get(v["produto"], 0) + v["quantidade"]
    return max(totais, key=totais.get)


def receita_total(vendas: List[Dict[str, Any]]) -> float:
    """Calcula a receita total de todas as vendas.

    Args:
        vendas (list): Lista de vendas.

    Returns:
        float: Receita total.

    Example:
        >>> receita_total([{"quantidade": 2, "valor_unit": 10.0}])
        20.0
    """
    return sum(v["quantidade"] * v["valor_unit"] for v in vendas)


vendas = json.loads(vendas_json)

for mes in ("Janeiro", "Fevereiro", "Março"):
    print(f"Total de {mes}: R$ {calcular_total_mes(vendas, mes):,.2f}")
print(f"Produto mais vendido: {produto_mais_vendido(vendas)}")
print(f"Receita total: R$ {receita_total(vendas):,.2f}")