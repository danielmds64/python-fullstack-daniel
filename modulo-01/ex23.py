import json

aluno = {
    "nome": "Pedro Henrique",
    "idade": 22,
    "curso": "Full Stack",
    "ativo": True,
    "notas": [8.5, 9.0, 7.5]
}

aluno_json = json.dumps(aluno, indent=2)
print(aluno_json)

aluno_dict = json.loads(aluno_json)

media = sum(aluno_dict["notas"]) / len(aluno_dict["notas"])
print(f"Nome: {aluno_dict['nome']}")
print(f"Média das notas: {media:.2f}")