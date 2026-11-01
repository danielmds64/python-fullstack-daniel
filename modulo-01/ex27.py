import json

funcionarios = [
    {"nome": "Ana Souza", "cargo": "Desenvolvedora", "salario": 7500.00, "departamento": "TI"},
    {"nome": "Bruno Lima", "cargo": "Analista", "salario": 5200.00, "departamento": "Financeiro"},
    {"nome": "Carla Dias", "cargo": "Gerente", "salario": 9800.00, "departamento": "RH"},
]

with open("funcionarios.json", "w", encoding="utf-8") as f:
    json.dump(funcionarios, f, indent=2, ensure_ascii=False)

with open("funcionarios.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

print(f"{'Nome':<15}{'Cargo':<18}{'Salário':>12}  {'Departamento':<12}")
print("-" * 60)
for func in dados:
    print(f"{func['nome']:<15}{func['cargo']:<18}{func['salario']:>12.2f}  {func['departamento']:<12}")

media = sum(func["salario"] for func in dados) / len(dados)
print("-" * 60)
print(f"Salário médio da equipe: R$ {media:.2f}")