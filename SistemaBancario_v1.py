menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

Escolha uma opção: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor Invalido!")

def efetuar_saque(valor):
    global saldo, limite, extrato, numero_saques, LIMITE_SAQUES
    if numero_saques < LIMITE_SAQUES:
        if valor <= saldo:
            if valor <= limite:
                saldo -= valor
                numero_saques += 1
                extrato += f"Saque: R$ {valor:.2f}\n"
                print("Saque Efetuado com Sucesso!")
            else:
                print(f"Seu limite maximo eh de R$ {limite:.2f} por saque")
        else:
            print("Saldo Insuficiente!")
    else:
        print("Limite de saques diários atingido! Volte amanhã.")

def mostra_extrato():
    print(f"Saldo: R$ {saldo:.2f}")
    print(extrato)

while True:
    opcao = input(menu)

    if opcao == "1":
        print("|------------- Depositar -------------|")
        valor = float(input("Digite o valor a ser depositado: "))
        depositar(valor)
    
    elif opcao == "2":
        print("|------------- Sacar -------------|")
        valor = float(input("Digite o valor a ser sacado: "))
        efetuar_saque(valor)
    
    elif opcao == "3":
        print("|------------- Extrato -------------|")
        mostra_extrato()

    elif opcao == "0":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")