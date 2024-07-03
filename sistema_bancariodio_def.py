#Autor: Lucas matheus
#Curso: Dio - Bootcamp Python & IA

# print exibindo nome do banco
print("""
      
      *******************  Bem Vindo  *******************
                       Banco de Brasília 
      ***************************************************
      """)
#declarando variáveis
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Exibindo o menu
menu = """
      ********************** MENU *************************
      1- Depositar
      2- Saque
      3- Extrato
      0- Sair
      *****************************************************
      """
#Mensagens prontas para imprimir na saida
mensagem1 = "Valor informado inválido! Tente novamente!"
mensagem2 = "Saque aprovado!"
mensagem3 = "Saldo insuficiente ou número de saques diários atingido!"
mensagem4 = "Opção inválida! Tente novamente!"

# Comando while(enquanto) para o loop!
while True:
    opcao = input(menu)
    # Estrutura de condicionais if/elif/else
    if opcao == "1":
        valor_deposito = float(input("Digite o valor de Depósito a ser efetuado: "))# recebe valor
        if valor_deposito > 0: 
            saldo += valor_deposito # verifica valor
            extrato += f"Depósito: R${valor_deposito:.2f}\n" #guarda valor em extrato
            print(f"Depósito de R${valor_deposito:.2f} efetuado com sucesso!") # print na tela valor de deposito
        else:
            print(mensagem1) # printa na tela caso algum valor esteja errado

    elif opcao == "2":
        valor_saque = float(input("""Digite o valor a ser sacado (limite de R$ 500,00 por saque): #recebe valor do saque
Você pode efetuar até 3 saques diários. 
Valor: R$ """))
        if valor_saque > 0 and valor_saque <= saldo and valor_saque <= limite and numero_saques < LIMITE_SAQUES:
            saldo -= valor_saque # verifica as condições para o saque
            extrato += f"Saque:{valor_saque:.2f}" # atualiza o extrato
            numero_saques += 1 # conta os saques
            print(mensagem2) #printa a mensagem na tela
        else:
            print(mensagem3)

      # Mostra as transações (movimentações do extrato da conta)
    elif opcao == "3":
        print("\n******************** EXTRATO DA CONTA *********************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("**************************************************************\n")
      # Sai do programa
    elif opcao == "0":
        print("Saindo... Obrigado por usar o Banco de Brasília!")
        break

    else:
        print(mensagem4)
