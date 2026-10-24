# ex18 - conversão de unidades encadeada

metros = int(input("Digite a distância em metros: "))

km = metros / 1000
cm = metros * 100
mm = metros * 1000
polegadas = metros * 39.3701
pes = metros * 3.2808

print(
    f"km{":":>8} {km:,.2f}\n"
    f"cm{":":>8} {cm:,.2f}\n"
    f"mm{":":>8} {mm:,.2f}\n"
    f"polegadas: {polegadas:,.2f}\n"
    f"pés{":":>7} {pes:,.2f}\n"
)