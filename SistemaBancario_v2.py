
def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor Invalido!")
    return saldo, extrato

def efetuar_saque(*, saldo, valor,extrato, limite,numero_saques, limite_saques):
    if numero_saques < limite_saques:
        if valor <= saldo:
            if valor <= limite:
                saldo -= valor
                numero_saques += 1
                extrato += f"Saque:\t\tR$ {valor:.2f}\n"
                print("Saque Efetuado com Sucesso!")
            else:
                print(f"Seu limite maximo eh de R$ {limite:.2f} por saque")
        else:
            print("Saldo Insuficiente!")
    else:
        print("Limite de saques diários atingido! Volte amanhã.")
    return saldo, extrato

def mostra_extrato(saldo, /, *, extrato):
    print(f"Saldo: R${saldo:.2f}")
    print(extrato)

def criar_conta(AGENCIA, numero_conta, usuarios):
    cpf = input("Informe seu CPF(Somente Numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("! Conta Criada com Sucesso !")
        return {"agencia":AGENCIA, "numero":numero_conta, "usuario":usuario}
    
    print("! Usuario nao encontrado !")
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t\t{conta['numero']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("="*100)
        print(linha)
    
def criar_usuario(usuarios):
    cpf = input("Informe seu CPF(Somente Numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("! Usuario Ja Cadastrado !")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nasc = input("Data de Nascimento(dd-mm-aaaa): ")
    endereco = input("Endereco (Rua, Nro, - Bairro - Cidade/SiglaEstado): ")

    usuarios.append({"nome":nome, "data_nasc":data_nasc, "endereco":endereco, "cpf":cpf})
    print("Usuario Cadastrado com Sucesso!")

def filtrar_usuario(cpf, usuarios):
    filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return filtrados[0] if filtrados else None

def main():
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []

    menu = """\n
    ============ MENU ============
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova Conta
    [5]\tListar Contas
    [6]\tNovo Usuario
    [0]\tSair

    Escolha uma opção: """

    while True:
        opcao = input(menu)

        if opcao == "1":
            print("|------------- Depositar -------------|")
            valor = float(input("Digite o valor a ser depositado: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "2":
            print("|------------- Sacar -------------|")
            valor = float(input("Digite o valor a ser sacado: "))
            saldo, extrato = efetuar_saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES
            )
        
        elif opcao == "3":
            print("|------------- Extrato -------------|")
            mostra_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            print("|------------- Adicionar Conta -------------|")
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "5":
            print("|------------- Listar Contas -------------|")
            listar_contas(contas)

        elif opcao == "6":
            print("|------------- Novo Usuario -------------|")
            criar_usuario(usuarios)

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida!")

main()