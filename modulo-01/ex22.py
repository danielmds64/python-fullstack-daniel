def calcular_area(largura: float, altura: float) -> float:
    return largura * altura

def formatar_nome(nome: str, sobrenome: str) -> str:
    return f"{nome} {sobrenome}".title()

def eh_maior_de_idade(idade: int) -> int:
    return idade >= 18

print(calcular_area(10, 20))
print(formatar_nome("Ronaldo", "Silva"))
print(eh_maior_de_idade(18))