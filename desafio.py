from time import sleep

dicionario_usuarios = []

numero_conta = 0

def fun_cpf_existe(cpfaux):

    cpf_existe = False
    cpf = cpfaux

    for usuario in dicionario_usuarios:

        if cpf == usuario["cpf"]:

            cpf_existe = True
            break

    return cpf_existe


def cadastrar_usuario():

    nome_usuario = input("Informe o nome do cliente: ")
    data_nascimento = input("Informe a data do nascimento: ")
    cpf = input("Informe o CPF: ")

    cpf_existe = fun_cpf_existe(cpf)

    if cpf_existe == False:

        endereco = input("Informe o seu endereço no formato (logradouro, N° - bairro - cidade/sigla estado)")
        dicio = {"nome": nome_usuario, "data do nascimento": data_nascimento, "cpf": cpf, "endereço": endereco, "contas" : []}

        dicionario_usuarios.append(dicio)
        print("Usuário cadastrado!")

    else:
         
         print("Usuário já possui cadastro!")


def exibir_usuarios():

    for usuarios in dicionario_usuarios:

        print(usuarios)


def vincular_conta():

    global numero_conta
    cpf = input("informe o CPF do usuário para Criar uma conta")
    variavel_cpf = fun_cpf_existe(cpf)

    if variavel_cpf == True:
        
        agencia = "0001"
        numero_conta += 1

        dicio_contas ={"agencia" : agencia, "numero_conta" : numero_conta, "saldo" : 0, "extrato" : ""}

        for usuario in dicionario_usuarios:

            if cpf == usuario["cpf"]:
                
                usuario["contas"].append(dicio_contas)
                print("Conta Cadastrada com sucesso!")
                sleep(1.5)
                break

    else:

        print("CPF não encontrado!")
        sleep(1)


def fun_conta_existe(cpf, num_conta):

    if fun_cpf_existe(cpf):
            
            for usuario in dicionario_usuarios:

                if cpf == usuario["cpf"]:
                    
                    for conta in usuario["contas"]:
                        
                        if num_conta == conta["numero_conta"]:

                            #print("depositar")
                            return True
    else:

        print("CPF não encontrado!")
        return False


def fun_sacar(*, cpf, num_conta, valor, limite, numero_saques):
    
    for usuario in dicionario_usuarios:

        if cpf == usuario["cpf"]:
            for conta in usuario["contas"]:
                if num_conta == conta["numero_conta"]:
                    if valor <= conta["saldo"] and valor <= limite and numero_saques <= 3:
                        conta["saldo"] -= valor
                        conta["extrato"] += f"Saque realizado no valor de R$ {valor}\n"


def fun_depositar(cpf,  num_conta, valor,/):
    
    for usuario in dicionario_usuarios:

        if cpf == usuario["cpf"]:
            for conta in usuario["contas"]:
                if num_conta == conta["numero_conta"]:
                    conta["saldo"] += valor
                    conta["extrato"] += f"Deposito realizado no valor de R$ {valor}\n"



def fun_ver_extrato(cpf, /, *, num_conta):

    for usuario in dicionario_usuarios:

        if cpf == usuario["cpf"]:
            for conta in usuario["contas"]:
                if num_conta == conta["numero_conta"]:
                    print(f"{conta["extrato"]}")


while True:
    print("""=========== MENU ==========
    [1] CADASTRAR USUÁRIO
    [2] VINCULAR CONTA
    [3] DEPOSITAR
    [4] SACAR
    [5] EXTRATO
    [6] VER USUÁRIOS
    [7] SAIR""")

    operacao_escolhida = int(input(""))

    if operacao_escolhida == 1:

        print(f"Cadastrar Usuário")
        cadastrar_usuario()
        sleep(2)

    elif operacao_escolhida == 2:

        print(f"Vincular Conta")
        vincular_conta()
        sleep(2)

    elif operacao_escolhida == 3:

        print(f"---------- DEPOSITAR ----------")
        cpf = input("Informe o CPF para depositar:")
        num_conta = int(input("Informe o número da conta: "))

        if fun_conta_existe(cpf, num_conta) == True:

            valor = float(input(f"Informe o valor para depositar:"))

            if valor > 0:

                fun_depositar(cpf, num_conta, valor)
            else:

                print(f" Valor inválido!")
        else:

            print("Essa conta não existe!")

        sleep(2)

    elif operacao_escolhida == 4:

        print(f"---------- SACAR ----------")
        cpf = input("Informe o CPF para sacar:")
        num_conta = int(input("Informe o número da conta: "))

        if fun_conta_existe(cpf, num_conta) == True:

            valor = float(input(f"Informe o valor para sacar:"))

            if valor > 0:

                fun_sacar(cpf= cpf, num_conta=num_conta, valor=valor, limite=500, numero_saques=0)

            else:

                print(f" Valor inválido!")
        else:

            print("Essa conta não existe!")
        
        sleep(1)

    elif operacao_escolhida == 5:

        print(f"---------- EXTRATO ----------")
        cpf = input("Informe o CPF para consultar extrato:")
        num_conta = int(input("Informe o número da conta: "))

        if fun_conta_existe(cpf, num_conta) == True:

            fun_ver_extrato(cpf, num_conta=num_conta)

        else:

            print("Essa conta não existe!")

        sleep(1)
    
    elif operacao_escolhida == 6:

        print(f"Exibir Usuários")
        exibir_usuarios()
        sleep(2)

    elif operacao_escolhida == 7:

        print(f"Saindo do Sistema")
        break

    else:

        print(f"Opção Inválida, volte ao MENU principal!")

        sleep(2)
    