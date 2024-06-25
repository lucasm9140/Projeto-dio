print("""
      
      *******************  Bem Vindo  *******************
                       Banco de Brasília 
      ***************************************************
      """)

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

menu = """
      ********************** MENU *************************
      1- Depositar
      2- Saque
      3- Extrato
      0- Sair
      *****************************************************
      """
mensagem1 = "Valor informado inválido! Tente novamente!"
mensagem2 = "Saque aprovado!"
mensagem3 = "Saldo insuficiente ou número de saques diários atingido!"
mensagem4 = "Opção inválida! Tente novamente!"

while True:
    opcao = input(menu)
    
    if opcao == "1":
        valor_deposito = float(input("Digite o valor de Depósito a ser efetuado: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R${valor_deposito:.2f}\n"
            print(f"Depósito de R${valor_deposito:.2f} efetuado com sucesso!")
        else:
            print(mensagem1)

    elif opcao == "2":
        valor_saque = float(input("""Digite o valor a ser sacado (limite de R$ 500,00 por saque):
Você pode efetuar até 3 saques diários. 
Valor: R$ """))
        if valor_saque > 0 and valor_saque <= saldo and valor_saque <= limite and numero_saques < LIMITE_SAQUES:
            saldo -= valor_saque
            extrato += f"Saque:{valor_saque:.2f}"
            numero_saques += 1
            print(mensagem2)
        else:
            print(mensagem3)

    elif opcao == "3":
        print("\n******************** EXTRATO DA CONTA *********************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("**************************************************************\n")

    elif opcao == "0":
        print("Saindo... Obrigado por usar o Banco de Brasília!")
        break

    else:
        print(mensagem4)
