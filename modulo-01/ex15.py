valor = float(input("Valor da compra: R$ "))
desconto = valor * 0.1
valor_final = valor - desconto

print(f"Valor da compra: R${valor:.2f}")
print(f"Valor do desconto: R${desconto:.2f}")
print(f"Valor final: R${valor_final:.2f}")