import json

produto = {
    "id": 101,
    "nome": "Fone Bluetooth",
    "preco": 199.90,
    "estoque": 35,
    "disponivel": True,
    "categorias": ["Eletrônicos", "Áudio", "Acessórios"],
}

with open("produto.json", "w", encoding="utf-8") as f:
    json.dump(produto, f, indent=2, ensure_ascii=False)

with open("produto.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

print(f"ID: {dados['id']}")
print(f"Nome: {dados['nome']}")
print(f"Preço: R$ {dados['preco']:.2f}")
print(f"Estoque: {dados['estoque']}")
print(f"Disponível: {dados['disponivel']}")
print(f"Categorias: {', '.join(dados['categorias'])}")