# ex17 - análise de nota fiscal

descricao = input("Digite a descrição do produto: ")
quantidade = int(input("Digite a quantidade do produto: "))
preco_un = float(input("Digite o preço unitário: R$ "))

print("\n")
print("===== NOTA FISCAL =====")
print(f"Produto   : {descricao}")
print(f"Quantidade: {quantidade} unidade(s)")
print(f"Preço Unit: R$ {preco_un:.2f}")
print(f"Subtotal  : R$ {quantidade * preco_un:.2f}")
print(f"Imposto   : R$ {quantidade * preco_un * 0.12:.2f}")
print(f"Total     : R$ {(quantidade * preco_un) + (quantidade * preco_un) * 0.12:.2f}")
print("=" * 23)
