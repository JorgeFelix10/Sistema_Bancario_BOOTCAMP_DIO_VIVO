from time import sleep


LIMITE_SAQUE = 500
QTD_SAQUES_DIARIO = 3
quantidade_saques = 0
saldo = 0
extrato = ""

while True:
    print("""
    ========== MENU ==========
          [1] DEPOSITAR
          [2] SACAR
          [3] EXTRATO
          [4] SAIR
          """)
    operaçao_escolhida = int(input(""))
    
    if operaçao_escolhida == 1:
        
        valor_depositado = float(input("Informe o valor que deseja depositar"))

        if valor_depositado <= 0:

            print("Não é possivel depositar valores negativos ou nulos!")
            print("Voltando ao MENU principal ...")
            sleep(1.5)
            
        else:

            saldo += float(valor_depositado)
            extrato += f"Depósito no valor de R$: {valor_depositado:.2f}\n"
            sleep(1.5)

    elif operaçao_escolhida == 2:

        valor_saque = float(input("Informe o valor que deseja sacar:"))

        if valor_saque <= saldo:

            if valor_saque <= LIMITE_SAQUE and quantidade_saques < 3:

                saldo -= valor_saque
                quantidade_saques += 1
                print("Saque bem sucedido!")
                extrato += f"Saque no valor de R$: {valor_saque:.2f}\n"
                sleep(1.5)
            else:
                print(f"Seu limite por saque é R$: {LIMITE_SAQUE:2f} e/ou voce só pode fazer {QTD_SAQUES_DIARIO} saques diários")
                print("Voltando ao MENU principal ...")
                sleep(1.5)

        else:
            print("Saldo insuficiente!")
            print("Voltando ao MENU principal ...")
            sleep(1.5)

    elif operaçao_escolhida == 3:

        print("========== EXTRATO ==========\n")
        print(f"{extrato}")
        print(f"Seu saldo atual é R$: {saldo:.2f}")
        sleep(1.5)

    elif operaçao_escolhida == 4:

        print("Saindo da conta")
        sleep(1.5)
        break

    else:
        print("Opção invalida!")
        print("Voltando ao MENU principal ...")
        sleep(1.5)
