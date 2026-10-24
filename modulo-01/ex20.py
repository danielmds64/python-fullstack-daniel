# ex20 - calculadora de investimentos simples

capital_inicial = float(input("Capital inicial: R$ "))
taxa_juros = float(input("Taxa de juros ao mês(%): ")) / 100
periodo = int(input("Digite o período em meses: "))

montante = capital_inicial * (1 + taxa_juros * periodo)

print("\n")
print(
    f"Capital inicial{":":>4} R$ {capital_inicial:,.2f}\n"
    f"Taxa de juros(mês){":":>} {taxa_juros * 100}%\n"
    f"Período{":":>12} {periodo} meses\n"
    f"Montante final{":":>5} R$ {montante:,.2f}"
)