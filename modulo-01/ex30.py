import json
from typing import List, TypedDict


class ItemPedido(TypedDict):
    produto: str
    quantidade: int
    preco_unitario: float


class Pedido(TypedDict):
    id_pedido: int
    cliente: str
    itens: List[ItemPedido]
    status: str


pedido: Pedido = {
    "id_pedido": 5001,
    "cliente": "Marina Alves",
    "itens": [
        {"produto": "Teclado Mecânico", "quantidade": 1, "preco_unitario": 349.90},
        {"produto": "Mouse Gamer", "quantidade": 2, "preco_unitario": 129.90},
    ],
    "status": "Em separação",
}

pedido_json = json.dumps(pedido, indent=2, ensure_ascii=False)
print(pedido_json)

total = sum(i["quantidade"] * i["preco_unitario"] for i in pedido["itens"])
print(f"\nTotal do pedido: R$ {total:.2f}")