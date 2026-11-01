from typing import Any, Dict, List


def validar_cadastro(dados: Dict[str, Any]) -> Dict[str, List[str]]:
    """Valida os dados de um cadastro.

    Regras: nome com ao menos 3 caracteres; email com '@' e '.'; idade
    entre 18 e 120; cpf com 11 dígitos numéricos.

    Args:
        dados (Dict[str, Any]): Dicionário com as chaves nome, email, idade e cpf.

    Returns:
        Dict[str, List[str]]: Dicionário com as chaves "valido" (campos
        aprovados) e "erros" (mensagens de erro).

    Example:
        >>> r = validar_cadastro({"nome": "Ana", "email": "a@b.com", "idade": 30, "cpf": "12345678901"})
        >>> r["erros"]
        []
    """
    valido: List[str] = []
    erros: List[str] = []

    nome = dados.get("nome", "")
    if isinstance(nome, str) and len(nome.strip()) >= 3:
        valido.append("nome")
    else:
        erros.append("nome deve ter ao menos 3 caracteres")

    email = dados.get("email", "")
    if isinstance(email, str) and "@" in email and "." in email:
        valido.append("email")
    else:
        erros.append("email deve conter '@' e '.'")

    idade = dados.get("idade")
    if isinstance(idade, int) and not isinstance(idade, bool) and 18 <= idade <= 120:
        valido.append("idade")
    else:
        erros.append("idade deve estar entre 18 e 120")

    cpf = dados.get("cpf", "")
    if isinstance(cpf, str) and len(cpf) == 11 and cpf.isdigit():
        valido.append("cpf")
    else:
        erros.append("cpf deve ter 11 dígitos numéricos")

    return {"valido": valido, "erros": erros}


dados_validos = {"nome": "Rafael Mendes", "email": "rafael@email.com", "idade": 28, "cpf": "12345678901"}
dados_invalidos = {"nome": "Jo", "email": "joemail.com", "idade": 15, "cpf": "123abc"}

print(validar_cadastro(dados_validos))
print(validar_cadastro(dados_invalidos))