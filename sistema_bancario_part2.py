#Instituição: Dio
#Aluno: Lucas Matheus
#Curso: Bootcamp python e IA

import getpass

print("""
      
      *******************  Bem Vindo  *******************
                       Banco de Brasília 
      ***************************************************
      """)

# Banco de dados simulado para armazenar usuários e suas contas
usuarios = {}

# Função para criar um novo usuário
def novo_usuario():
    global usuarios
    nome = input("Digite seu nome: ")
    if nome in usuarios:
        print("Usuário já existe!")
        return None
    senha = getpass.getpass("Digite sua senha: ")
    usuarios[nome] = {'senha': senha, 'contas': []}
    print(f"Usuário {nome} criado com sucesso!")
    return nome

# Função para criar uma nova conta
def nova_conta(usuario):
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    conta = {'saldo': saldo, 'limite': limite, 'extrato': extrato, 'numero_saques': numero_saques, 'LIMITE_SAQUES': LIMITE_SAQUES}
    usuarios[usuario]['contas'].append(conta)
    print(f"Conta criada com sucesso para {usuario}!")
    return conta

# Função para realizar login
def login():
    nome = input("Digite seu nome: ")
    if nome not in usuarios:
        print("Usuário não encontrado!")
        return None, None
    senha = getpass.getpass("Digite sua senha: ")
    if usuarios[nome]['senha'] != senha:
        print("Senha incorreta!")
        return None, None
    print(f"Login bem-sucedido! Bem-vindo, {nome}!")
    return nome, usuarios[nome]['contas'][0]  # Considerando que cada usuário tem pelo menos uma conta

# Menu principal
menu_principal = """
      ********************** MENU PRINCIPAL *************************
      1- Novo Usuário
      2- Login
      0- Sair
      ***************************************************************
      """

# Menu de operações bancárias
menu_bancario = """
      ********************** MENU *************************
      1- Depositar
      2- Saque
      3- Extrato
      0- Sair
      *****************************************************
      """

# Mensagens de feedback
mensagem1 = "Valor informado inválido! Tente novamente!"
mensagem2 = "Saque aprovado!"
mensagem3 = "Saldo insuficiente ou número de saques diários atingido!"
mensagem4 = "Opção inválida! Tente novamente!"

# Loop principal para o menu principal
while True:
    opcao_principal = input(menu_principal)
    
    if opcao_principal == "1":
        usuario = novo_usuario()
        if usuario:
            conta = nova_conta(usuario)

    elif opcao_principal == "2":
        usuario, conta = login()
        if usuario:
            while True:
                opcao = input(menu_bancario)
                
                if opcao == "1":
                    valor_deposito = float(input("Digite o valor de Depósito a ser efetuado: "))
                    if valor_deposito > 0:
                        conta['saldo'] += valor_deposito
                        conta['extrato'] += f"Depósito: R${valor_deposito:.2f}\n"
                        print(f"Depósito de R${valor_deposito:.2f} efetuado com sucesso!")
                    else:
                        print(mensagem1)

                elif opcao == "2":
                    valor_saque = float(input("""Digite o valor a ser sacado (limite de R$ 500,00 por saque):
Você pode efetuar até 3 saques diários. 
Valor: R$ """))
                    if valor_saque > 0 and valor_saque <= conta['saldo'] and valor_saque <= conta['limite'] and conta['numero_saques'] < conta['LIMITE_SAQUES']:
                        conta['saldo'] -= valor_saque
                        conta['extrato'] += f"Saque: R${valor_saque:.2f}\n"
                        conta['numero_saques'] += 1
                        print(mensagem2)
                    else:
                        print(mensagem3)

                elif opcao == "3":
                    print("\n******************** EXTRATO DA CONTA *********************")
                    print("Não foram realizadas movimentações." if not conta['extrato'] else conta['extrato'])
                    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
                    print("**************************************************************\n")

                elif opcao == "0":
                    print("Saindo... Obrigado por usar o Banco de Brasília!")
                    break

                else:
                    print(mensagem4)

    elif opcao_principal == "0":
        print("Saindo... Obrigado por usar o Banco de Brasília!")
        break

    else:
        print("Opção inválida! Tente novamente.")
