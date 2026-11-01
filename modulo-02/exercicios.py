"""
=============================================================
MÓDULO 2 – Estruturas de Controle
Curso de Capacitação Full Stack – ITEAM

Aluno(a): DANIEL MEDEIROS DA SILVA
Data    : <DATA DE ENTREGA>
=============================================================

INSTRUÇÕES:
  1. Substitua <SEU NOME COMPLETO AQUI> e <DATA DE ENTREGA> acima.
  2. Implemente cada função no espaço indicado com # SUA SOLUÇÃO AQUI.
  3. Não apague os comentários de orientação.
  4. Execute o arquivo para testar suas soluções antes de enviar.
  5. Salve este arquivo como modulo-02/exercicios.py, na sua cópia
     do repositório do curso.

COMO EXECUTAR:
  python exercicios.py
=============================================================
"""


# ==============================================================
# EXERCÍCIO 01 – Classificador de Temperatura
# Conceitos: if / elif / else, float(), input()
# ==============================================================
def ex01_classificador_temperatura():
    """
    Lê uma temperatura em Celsius e exibe sua classificação.

    Faixas:
        < 0        → ❄️ Congelante
        0  a 14   → 🥶 Frio
        15 a 24   → 😊 Agradável
        25 a 34   → ☀️ Quente
        >= 35     → 🔥 Muito quente
    """
    # SUA SOLUÇÃO AQUI
    temperatura = float(input("Temperatura em Celsius: "))

    if temperatura < 0:
        print("Congelante")
    elif temperatura <= 14:
        print("Frio")
    elif temperatura <= 24:
        print("Agradável")
    elif temperatura <= 34:
        print("Quente")
    else:
        print("Muito quente")
    pass


# ==============================================================
# EXERCÍCIO 02 – Validador de Acesso
# Conceitos: if aninhado, comparação de strings
# ==============================================================
def ex02_validador_acesso():
    """
    Solicita usuário e senha e valida o acesso.

    Credenciais corretas:
        usuário → "admin"
        senha   → "iteam2025"
    """
    # SUA SOLUÇÃO AQUI
    usuario = "admin"
    senha = "iteam2025"

    tentativa_usuario = input("Digite o usuário: ")
    tentativa_senha = input("Digite a senha: ")

    if tentativa_usuario == usuario and tentativa_senha == senha:
        print("Acesso liberado. Bem-vindo!")
    elif tentativa_usuario != usuario:
        print("Usuário não encontrado")
    else: 
        print("Senha incorreta")
    pass


# ==============================================================
# EXERCÍCIO 03 – Tabuada Interativa
# Conceitos: for, range(), f-string com alinhamento
# ==============================================================
def ex03_tabuada():
    """
    Solicita um número inteiro e exibe sua tabuada de 1 a 10.
    """
    # SUA SOLUÇÃO AQUI
    n = int(input("Número: "))

    print(f"=== Tabuada do {n} ===")

    for i in range(1, 10+1):
        print(f"{n} x {i} = {n * i}")
    pass


# ==============================================================
# EXERCÍCIO 04 – Contador Regressivo
# Conceitos: while, print com end=
# ==============================================================
def ex04_contador_regressivo():
    """
    Solicita um número inteiro positivo e faz a contagem
    regressiva até 0, finalizando com '🚀 Lançamento!'.
    """
    # SUA SOLUÇÃO AQUI
    num = int(input("Número: "))

    while num >= 0:
        print(num, end=", ")
        num -= 1

    print("Lançamento!")
    pass


# ==============================================================
# EXERCÍCIO 05 – Buscador com break
# Conceitos: for, break, enumerate()
# ==============================================================
def ex05_buscador_break():
    """
    Percorre o estoque e localiza 'Monitor', exibindo
    sua posição. Usa break ao encontrar o item.
    """
    estoque = ["Teclado", "Mouse", "Webcam", "Monitor", "Headset", "Notebook"]

    # SUA SOLUÇÃO AQUI
    posicao = 0
    for item in estoque:
        posicao += 1
        if item == "Monitor":
            break
    print(f"O item foi encontrado na posição de número {posicao}")
    pass


# ==============================================================
# EXERCÍCIO 06 – Filtro de Dados com continue
# Conceitos: for, continue, None, acumuladores
# ==============================================================
def ex06_filtro_continue():
    """
    Percorre a lista de leituras, ignora os valores None
    com continue e calcula soma, média e total ignorado.
    """
    leituras = [12.5, None, 8.3, None, 15.0, 9.7, None, 11.2, 6.8, None]

    # SUA SOLUÇÃO AQUI
    soma = 0
    quantidade = 0
    registros_ignorados = 0
    for item in leituras:
        if item is None:
            registros_ignorados += 1
            continue
        quantidade += 1
        soma += item
    media = soma / quantidade
    print(f"A soma dos valores válidos é: {soma:.2f}")
    print(f"A média dos valores válidos é: {media:.2f}")
    print(f"Total de registros ignorados: {registros_ignorados}")
    pass


# ==============================================================
# EXERCÍCIO 07 – Validação de Entrada com while
# Conceitos: while True, break, if/elif/else, float()
# ==============================================================
def ex07_validacao_nota():
    """
    Solicita a nota do aluno repetidamente até receber
    um valor válido (0.0 a 10.0), então exibe o conceito.

    Conceitos:
        9.0 a 10.0 → A – Excelente
        7.0 a 8.9  → B – Bom
        5.0 a 6.9  → C – Regular
        < 5.0      → D – Insuficiente
    """
    # SUA SOLUÇÃO AQUI
    while True:
        nota = float(input("Digite a nota: "))
        if nota < 0 or nota > 10:
            print("Valor inválido. Tente novamente")
        else:
            break
    
    print("Nota | Conceito")
    if nota >= 9:
        print(f"{nota} | A - Excelente")
    elif nota >= 7:
        print(f"{nota} | B - Bom")
    elif nota >= 5:
        print(f"{nota} | C - Regular")
    else:
        print(f"{nota} | D - Insuficiente")
    pass


# ==============================================================
# EXERCÍCIO 08 – Calculadora com try/except
# Conceitos: try/except/else/finally, ValueError, ZeroDivisionError
# ==============================================================
def ex08_calculadora_segura():
    """
    Solicita dois números e uma operação (+, -, *, /).
    Trata: ValueError, ZeroDivisionError, operação inválida.
    Usa else para exibir o resultado e finally para encerrar.
    """
    # SUA SOLUÇÃO AQUI\
    try:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        operacao = int(input("Digite um número para escolher a operação [1. +] [2. -] [3. *] [4. /]: "))
        if operacao < 1 or operacao > 4:
            print("Operação inválida.")
    except ValueError:
        print("Digite apenas números!")
    else:
        if operacao == 1:
            print(f"Soma = {n1 + n2}")
        elif operacao == 2:
            print(f"Subtração = {n1 - n2}")
        elif operacao == 3:
            print(f"Multiplicação = {n1 * n2}")
        else: 
            try:
                print(f"Divisão = {n1 / n2}")
            except ZeroDivisionError:
                print("Erro: divisão por 0!")
    pass


# ==============================================================
# EXERCÍCIO 09 – Padrão Numérico com for aninhado
# Conceitos: for aninhado, range(), print com end=
# ==============================================================
def ex09_padrao_numerico():
    """
    Gera o triângulo crescente:
        1
        1 2
        1 2 3
        ...
        1 2 3 4 5

    Desafio extra: gera também o triângulo decrescente logo abaixo.
    """
    # SUA SOLUÇÃO AQUI
    for i in range(6):
        for j in range(i):
            print(f"{j+1}", end=" ")
        print()

    for i in range(5, 0, -1):
        for j in range(i):
            print(f"{j+1}", end=" ")
        print()
    pass


# ==============================================================
# EXERCÍCIO 10 – Jogo de Adivinhação
# Conceitos: while, contador, random, if/elif/else
# ==============================================================
def ex10_jogo_adivinhacao():
    """
    O computador sorteia um número entre 1 e 100.
    O usuário tem 7 tentativas para adivinhar.
    A cada erro, indica se o número é maior ou menor.
    """
    import random
    numero_secreto = random.randint(1, 100)

    # SUA SOLUÇÃO AQUI
    contador = 0
    while contador < 7:
        contador += 1
        tentativa = int(input("Digite um número: "))
        if tentativa == numero_secreto:
            print(f"🎉 Parabéns! Você acertou em {contador} tentativas.")
            return 0
        else:
            print("Errado! Tente novamente.")

    print(f"💀 Game over! O número era {numero_secreto}.")
    pass


# ==============================================================
# EXERCÍCIO 11 – Verificador de Número Primo
# Conceitos: for, break, try/except, otimização com √n
# ==============================================================
def ex11_numero_primo():
    """
    Solicita um número inteiro positivo e verifica se é primo.
    Usa break ao encontrar o primeiro divisor.
    Trata ValueError e números negativos/zero.
    Otimização: verifica divisores somente até √n.
    """
    # SUA SOLUÇÃO AQUI
    try:
        num = int(input("Digite um número: "))
        if num <= 0:
            raise ValueError
    except ValueError:
        print("O valor precisa ser um número inteiro positivo!")
        return

    if num < 2:
        print(f"{num} não é primo. ❌")
        return

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} não é primo. Divisível por {i}. ❌")
            break
    else:
        print(f"{num} é um número primo. ✅")


# ==============================================================
# EXERCÍCIO 12 – Analisador de Senha Forte
# Conceitos: for, if, booleanos, métodos de string
# ==============================================================
def ex12_analisador_senha():
    """
    Analisa se uma senha atende aos critérios de segurança:
        - Mínimo 8 caracteres
        - Pelo menos 1 maiúscula
        - Pelo menos 1 minúscula
        - Pelo menos 1 dígito
        - Pelo menos 1 caractere especial: !@#$%^&*

    Exibe relatório com ✅ ou ❌ para cada critério.
    """
    # SUA SOLUÇÃO AQUI
    senha = input("Digite a senha: ")
    especiais = "!@#$%^&*"

    tem_maiuscula = False
    tem_minuscula = False
    tem_digito = False
    tem_especial = False

    for c in senha:
        if c.isupper():
            tem_maiuscula = True
        elif c.islower():
            tem_minuscula = True
        elif c.isdigit():
            tem_digito = True
        elif c in especiais:
            tem_especial = True

    tamanho_ok = len(senha) >= 8

    print(f"\nAnalisando: {senha}")
    print(("✅" if tamanho_ok else "❌") + f" Comprimento {'adequado' if tamanho_ok else 'insuficiente'} ({len(senha)} caracteres)")
    print(("✅" if tem_maiuscula else "❌") + " Contém maiúscula")
    print(("✅" if tem_minuscula else "❌") + " Contém minúscula")
    print(("✅" if tem_digito else "❌") + " Contém número")
    print(("✅" if tem_especial else "❌") + " Contém caractere especial")

    if tamanho_ok and tem_maiuscula and tem_minuscula and tem_digito and tem_especial:
        print("🔒 Senha FORTE!")
    else:
        print("⚠️ Senha FRACA!")


# ==============================================================
# EXERCÍCIO 13 – Simulador de Caixa Eletrônico
# Conceitos: while, //, if/else, try/except
# ==============================================================
def ex13_caixa_eletronico():
    """
    Solicita um valor de saque (múltiplo de R$10, máx R$3.000).
    Calcula o menor número de cédulas: R$200, R$100, R$50, R$20, R$10.
    Trata entradas inválidas.
    """
    cedulas = [200, 100, 50, 20, 10]

    # SUA SOLUÇÃO AQUI
    try:
        valor = int(input("Digite o valor do saque: R$ "))
    except ValueError:
        print("Digite apenas números inteiros!")
        return

    if valor <= 0:
        print("O valor deve ser maior que zero!")
    elif valor % 10 != 0:
        print("O valor deve ser múltiplo de 10!")
    elif valor > 3000:
        print("O limite máximo de saque é R$ 3.000!")
    else:
        print(f"\n💵 Saque: R$ {valor}")
        print("Cédulas utilizadas:")
        restante = valor
        total = 0
        i = 0
        while i < len(cedulas):
            qtd = restante // cedulas[i]
            if qtd > 0:
                print(f"  R${cedulas[i]:<3} → {qtd} cédula(s)")
                total += qtd
                restante -= qtd * cedulas[i]
            i += 1
        print(f"Total de cédulas: {total}")


# ==============================================================
# EXERCÍCIO 14 – Leitura de Múltiplos Dados com Tratamento
# Conceitos: while, break, continue, try/except, pass
# ==============================================================
def ex14_leitura_notas_turma():
    """
    Lê notas de uma turma até o usuário digitar 'fim'.
    Ignora notas inválidas com continue + mensagem de aviso.
    Ao encerrar, exibe: total, média, maior e menor nota.
    """
    notas = []

    # SUA SOLUÇÃO AQUI
    while True:
        entrada = input("Digite uma nota (0-10) ou 'fim': ").strip()

        if entrada.lower() == "fim":
            break

        try:
            nota = float(entrada.replace(",", "."))
        except ValueError:
            print("⚠️ Entrada inválida! Digite um número ou 'fim'.")
            continue

        if nota < 0 or nota > 10:
            print("⚠️ Nota fora do intervalo! Digite um valor entre 0 e 10.")
            continue

        notas.append(nota)

    if notas:
        print(f"\nTotal de notas válidas: {len(notas)}")
        print(f"Média: {sum(notas) / len(notas):.2f}")
        print(f"Maior nota: {max(notas):.2f}")
        print(f"Menor nota: {min(notas):.2f}")
    else:
        print("\nNenhuma nota válida foi informada.")


# ==============================================================
# EXERCÍCIO 15 – Desafio Final: Menu de Sistema
# Conceitos: while True, if/elif/else, break, continue, try/except
# ==============================================================
def ex15_menu_sistema():
    """
    Menu interativo que permanece ativo até o usuário sair.

    Opções:
        [1] Conversor de temperatura (Celsius → Fahrenheit)
        [2] Verificador de número primo (versão simplificada)
        [3] Analisador de senha (apenas comprimento e dígito)
        [4] Calculadora segura (só +, -, *, /)
        [0] Sair

    Usa try/except em toda entrada do usuário.
    """
    while True:
        print("\n" + "=" * 29)
        print("   SISTEMA ITEAM - MENU    ")
        print("=" * 29)
        print("[1] Conversor de temperatura")
        print("[2] Verificador de número primo")
        print("[3] Analisador de senha")
        print("[4] Calculadora segura")
        print("[0] Sair")
        print("=" * 29)

        # SUA SOLUÇÃO AQUI — leia a opção e implemente cada funcionalidade
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("⚠️ Digite um número válido!")
            continue

        if opcao == 0:
            print("Encerrando o sistema. Até logo! 👋")
            break

        elif opcao == 1:
            try:
                celsius = float(input("Temperatura em Celsius: "))
            except ValueError:
                print("⚠️ Valor inválido!")
                continue
            fahrenheit = celsius * 9 / 5 + 32
            print(f"{celsius:.1f}°C = {fahrenheit:.1f}°F")

        elif opcao == 2:
            try:
                num = int(input("Digite um número: "))
            except ValueError:
                print("⚠️ Valor inválido!")
                continue
            if num < 2:
                print(f"{num} não é primo. ❌")
                continue
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    print(f"{num} não é primo. Divisível por {i}. ❌")
                    break
            else:
                print(f"{num} é um número primo. ✅")

        elif opcao == 3:
            try:
                senha = input("Digite a senha: ")
            except EOFError:
                print("⚠️ Entrada inválida!")
                continue
            tem_digito = False
            for c in senha:
                if c.isdigit():
                    tem_digito = True
                    break
            print(("✅" if len(senha) >= 8 else "❌") + f" Comprimento ({len(senha)} caracteres)")
            print(("✅" if tem_digito else "❌") + " Contém número")
            if len(senha) >= 8 and tem_digito:
                print("🔒 Senha aceita!")
            else:
                print("⚠️ Senha fraca!")

        elif opcao == 4:
            try:
                a = float(input("Primeiro número: "))
                op = input("Operação (+, -, *, /): ").strip()
                b = float(input("Segundo número: "))
            except ValueError:
                print("⚠️ Valor inválido!")
                continue
            if op == "+":
                print(f"Resultado: {a + b}")
            elif op == "-":
                print(f"Resultado: {a - b}")
            elif op == "*":
                print(f"Resultado: {a * b}")
            elif op == "/":
                try:
                    print(f"Resultado: {a / b}")
                except ZeroDivisionError:
                    print("⚠️ Não é possível dividir por zero!")
            else:
                print("⚠️ Operação inválida!")

        else:
            print("⚠️ Opção inválida! Escolha entre 0 e 4.")
            continue


# ==============================================================
# EXECUÇÃO PRINCIPAL
# Descomente as chamadas dos exercícios que você já resolveu.
# ==============================================================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("MÓDULO 2 – Estruturas de Controle")
    print(f"Aluno(a): DANIEL MEDEIROS DA SILVA")
    print("=" * 50)

    # Descomente linha por linha conforme for resolvendo:
    #ex01_classificador_temperatura()
    #ex02_validador_acesso()
    #x03_tabuada()
    #ex04_contador_regressivo()
    #ex05_buscador_break()
    #ex06_filtro_continue()
    #ex07_validacao_nota()
    #ex08_calculadora_segura()
    #ex09_padrao_numerico()
    #ex10_jogo_adivinhacao()
    #ex11_numero_primo()
    #ex12_analisador_senha()
    #ex13_caixa_eletronico()
    #ex14_leitura_notas_turma()
    #ex15_menu_sistema()