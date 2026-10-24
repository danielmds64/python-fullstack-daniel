# ex19 - manipulação de strings no mundo real

email = " joao.silva@EMPRESA.com.br "
email = email.strip().lower()

usuario = email.split("@")[0]
dominio = email.split("@")[1]

print(
    f"Email: {email}\n"
    f"Usuário: {usuario}\n"
    f"Domínio: {dominio}\n"
)