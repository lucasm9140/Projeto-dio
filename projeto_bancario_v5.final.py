#Aluno: Lucas matheus
#Curso: DIO - Bootcamp Python & IA

# biblioteca datetime - fornece ferramentas para comunicação de hora e data!
from datetime import datetime
# classe usuario verifica os digitos do cpf e armazena os 
# valores(nome, cpf, contas, corrente, poupança e credito especial!)
class Usuario:
    def __init__(self, nome, cpf):
        if len(cpf) != 11:
            raise ValueError("CPF deve ter exatamente 11 dígitos.")
        self.nome = nome
        self.cpf = cpf
        self.contas = {
            'corrente': None,
            'poupanca': None,
            'credito_especial': None
        }
#def - Definição para adicionar conta
    def adicionar_conta(self, tipo_conta, conta):
        self.contas[tipo_conta] = conta
#def - listar contas - corrente, poupança, credito especial
    def listar_contas(self):
        return self.contas
#def - recebe o cpf e o retorna quando se torna necessário
    def get_cpf(self):
        return self.cpf
#def - Definição para uma string - retornando nome(nome de usuario) e cpf
    def __str__(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}"

class Banco:
    def __init__(self, nome_banco): 
        #função que cria o objeto da classe - com o init - construtor!
        self.nome_banco = nome_banco 
        self.usuarios = []
        # def - função para adicionar usuário
    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)
        # def - função que verifica se tem usuario cadastrado
    def listar_usuarios(self):
        if not self.usuarios: 
        # if not - negando se não tiver o nome de usuario cadastrado, 
        # retorna o print("Não há usuários cadastrados")
            print("Não há usuários cadastrados.")
        else:
        # negativa, negando a negativa do if not, caso tenha usuário mostra na tela
        # nome de usuario e cpf
            print(f"\nUsuários do {self.nome_banco}:")
            for usuario in self.usuarios:
                print(f"- {usuario.nome} ({usuario.cpf})")
# definição para criar conta corrente 
    def criar_conta_corrente(self, usuario, numero_conta, saldo_inicial=0, limite_cheque_especial=1000):
        if usuario.contas['corrente'] is None: # if else para verificar se ja tem conta 
            conta = ContaCorrente(numero_conta, saldo_inicial, limite_cheque_especial)
            usuario.adicionar_conta('corrente', conta)
            return conta # retorna os valores inseridos pelo usuário a função
        else: # else para negar nova conta se ja ouver uma conta.
            print(f"O usuário {usuario.nome} já possui uma conta corrente.")
            return None
# definição para criar uma função para criar conta corrente
    def criar_conta_poupanca(self, usuario, numero_conta, saldo_inicial=0):
        if usuario.contas['poupanca'] is None: # if else para verificar se ja tem conta 
            conta = ContaPoupanca(numero_conta, saldo_inicial)
            usuario.adicionar_conta('poupanca', conta)
            return conta # retorna os valores inseridos pelo usuário a função
        else: # else para negar nova conta se ja ouver uma conta.
            print(f"O usuário {usuario.nome} já possui uma conta poupança.")
            return None
# definição para criar outra função para criar conta de credito especial
    def criar_credito_especial(self, usuario, numero_conta, saldo_inicial=0, limite_credito_especial=2000):
        if usuario.contas['credito_especial'] is None: # if else para verificar se ja tem conta 
            conta = CreditoEspecial(numero_conta, saldo_inicial, limite_credito_especial)
            usuario.adicionar_conta('credito_especial', conta)
            return conta #retorna os valores inseridos pelo usuário a função
        else:  # else para negar nova conta se ja ouver uma conta.
            print(f"O usuário {usuario.nome} já possui uma conta de crédito especial.")
            return None
# definição para criar mais uma função verificar o limite de saques
    def verificar_limite_saques(self, conta):
        if conta.get_numero_saques() >= 3: # if verificando se os saques efetuados foram igual a 3
            print("Limite diário de saques atingido para esta conta.")
            return False # se chegou a 3 printa e retorna a mensagem acima
        else:
            return True # retorna confimando o limite do saque diario

# classe conta bancaria recebe numero da conta na função init - bloco construtor
class ContaBancaria:
    def __init__(self, numero_conta, saldo_inicial=0):
        self._numero_conta = numero_conta
        self._saldo = saldo_inicial
        self._extrato = []
        self._numero_saques = 0
# def - função depositar
    def depositar(self, valor):
        if valor > 0: # if verifica se o valor é maior que zero
            self._saldo += valor # atribui o saldo com valor do deposito
            # atualiza o extrato - e registra a transação
            self._extrato.append((datetime.now(), f"Depósito: R$ {valor:.2f}"))
            print(f"Depósito de R$ {valor:.2f} efetuado com sucesso na conta {self._numero_conta}!")
            # print do valor do deposito e da transação na conta
        else:
            # se for invalido o valor informado apresenta essa mensagem na tela
            print("Valor informado inválido! Tente novamente!")
# definindo uma função sacar
    def sacar(self, valor):
        # falta resolver esse metodo que ainda não foi devidamente finalizado
        raise NotImplementedError("Método sacar() deve ser implementado nas subclasses!")
# outra definição de imprimir extrato
    def imprimir_extrato(self):
        if not self._extrato: # se não tiver movimentações exibi o print com a mensagem
            print(f"\n******************** EXTRATO DA CONTA {self._numero_conta} *********************")
            print("Não foram realizadas movimentações.")
        else: # se ouver mostra as movimentações no extrato da conta
            print(f"\n******************** EXTRATO DA CONTA {self._numero_conta} *********************")
            for data, movimentacao in self._extrato:
                print(f"{data.strftime('%d/%m/%Y %H:%M:%S')} - {movimentacao}")
        print(f"\nSaldo: R$ {self._saldo:.2f}")
        print("**************************************************************\n")
# definição de uma função para tranferir para outra conta
    def transferir(self, valor, conta_destino):
        if valor > 0 and self._saldo >= valor: # verifica se o valor é maior que zero
            self._saldo -= valor # decrementa o valor do saldo
            conta_destino.depositar(valor) # transfere e armazena o valor
            self._extrato.append((datetime.now(), f"Transferência enviada para {conta_destino.get_numero_conta()}: R$ {valor:.2f}"))
            # exibi a movimentação das transferencia
            print(f"Transferência de R$ {valor:.2f} para conta {conta_destino.get_numero_conta()} efetuada com sucesso!")
        else:
            print("Transferência não realizada. Verifique o saldo ou o valor informado.")
            # se a transferencia não realizada recebe a mensagem do print do else
# definição do saldo ta recebendo e retornando           
    def get_saldo(self):
        return self._saldo
# definição numero da conta recebe e guarda
    def get_numero_conta(self):
        return self._numero_conta
# definição numero de saques
    def get_numero_saques(self):
        return self._numero_saques

# classe da conta corrente
class ContaCorrente(ContaBancaria): 
    # função inicio de objeto
    def __init__(self, numero_conta, saldo_inicial=0, limite_cheque_especial=1000):
        super().__init__(numero_conta, saldo_inicial)
        self._limite_cheque_especial = limite_cheque_especial
    # função sacar
    def sacar(self, valor):
        if valor > 0 and valor <= 500 and (self._saldo + self._limite_cheque_especial) >= valor:
            if self._saldo >= valor:
                self._saldo -= valor
                self._extrato.append((datetime.now(), f"Saque: R$ {valor:.2f}"))
                self._numero_saques += 1
                print(f"Saque de R$ {valor:.2f} na conta corrente {self._numero_conta} aprovado!")
            else:
                valor_saque = valor - self._saldo
                self._saldo = 0
                self._limite_cheque_especial -= valor_saque
                self._extrato.append((datetime.now(), f"Saque: R$ {valor:.2f} (utilizado cheque especial)"))
                self._numero_saques += 1
                print(f"Saque de R$ {valor:.2f} na conta corrente {self._numero_conta} aprovado utilizando cheque especial.")
        else:
            print("Saque não realizado. Verifique o valor ou o saldo disponível.")
# função imprimir extrato - cheque especial
    def imprimir_extrato(self):
        super().imprimir_extrato()
        print(f"Limite do Cheque Especial da conta {self._numero_conta}: R$ {self._limite_cheque_especial:.2f}")

# classe conta poupança
class ContaPoupanca(ContaBancaria):
    # função de inicio de objeto
    def __init__(self, numero_conta, saldo_inicial=0):
        super().__init__(numero_conta, saldo_inicial)
        self._rendimento_mensal = 0.5  # Porcentagem
    # função calcular o rendimento da poupança
    def calcular_rendimento(self):
        rendimento = self._saldo * (self._rendimento_mensal / 100)
        self._saldo += rendimento
        self._extrato.append((datetime.now(), f"Rendimento Poupança: R$ {rendimento:.2f}"))
        print(f"Rendimento mensal de R$ {rendimento:.2f} aplicado à poupança {self._numero_conta}.")
    # função sacar - da poupança
    def sacar(self, valor):
        if valor > 0 and valor <= 500 and self._saldo >= valor:
            self._saldo -= valor
            self._extrato.append((datetime.now(), f"Saque: R$ {valor:.2f}"))
            self._numero_saques += 1
            print(f"Saque de R$ {valor:.2f} na poupança {self._numero_conta} aprovado!")
        else:
            print("Saque não realizado. Verifique o valor ou o saldo disponível.")

# classe credito especial
class CreditoEspecial(ContaBancaria):
    def __init__(self, numero_conta, saldo_inicial=0, limite_credito_especial=2000):
        super().__init__(numero_conta, saldo_inicial)
        self._limite_credito_especial = limite_credito_especial
    # função sacar do limite de credito especial
    def sacar(self, valor):
        if valor > 0 and valor <= 500 and (self._saldo + self._limite_credito_especial) >= valor:
            if self._saldo >= valor:
                self._saldo -= valor
                self._extrato.append((datetime.now(), f"Saque: R$ {valor:.2f}"))
                self._numero_saques += 1
                print(f"Saque de R$ {valor:.2f} na conta crédito especial {self._numero_conta} aprovado!")
            else:
                valor_saque = valor - self._saldo
                self._saldo = 0
                self._limite_credito_especial -= valor_saque
                self._extrato.append((datetime.now(), f"Saque: R$ {valor:.2f} (utilizado crédito especial)"))
                self._numero_saques += 1
                print(f"Saque de R$ {valor:.2f} na conta crédito especial {self._numero_conta} aprovado utilizando crédito especial.")
        else:
            print("Saque não realizado. Verifique o valor ou o saldo disponível.")
    # função imprimir extrato do credito especial
    def imprimir_extrato(self):
        super().imprimir_extrato()
        print(f"Limite do Crédito Especial da conta {self._numero_conta}: R$ {self._limite_credito_especial:.2f}")

# função main - apresenta o nome do banco
def main():
    banco = Banco("Banco de Brasília")
    # loop para aparecer o nome do banco junto com o menu
    while True:
        print("""
        *******************  Bem Vindo  *******************
                        Banco de Brasília 
        ***************************************************
        """)

        menu_principal = """
        ********************** MENU *************************
        1- Adicionar novo usuário
        2- Criar conta corrente
        3- Criar conta poupança
        4- Criar conta crédito especial
        5- Listar usuários
        6- Listar contas de um usuário
        7- Realizar operações bancárias
        0- Sair
        *****************************************************
        """

        opcao = input(menu_principal)
# if e else com opções primeiro usuario depois senha
        if opcao == "1":
            while True:
                nome = input("Digite o nome do novo usuário (deve ter exatamente 5 letras): ")
                if len(nome) == 5:
                    break
                else:
                    print("O nome do usuário deve ter exatamente 5 letras.")
            # outro loop para o cpf
            while True:
                cpf = input("Digite o CPF do novo usuário (11 dígitos): ")
                if len(cpf) == 11 and cpf.isdigit(): # verifica se tem 11 digitos e so numeros
                    break
                else:
                    print("CPF deve ter exatamente 11 dígitos.")
            novo_usuario = Usuario(nome, cpf) # se não tiver cadastro de usuário leva para cadastrar novo usuario
            banco.adicionar_usuario(novo_usuario) # adicionar novo usuario armazena o valor
            print(f"Usuário {nome} cadastrado com sucesso!")
# opção para criar a conta corrente
        elif opcao == "2":
            cpf = input("Digite o CPF do usuário para criar a conta corrente: ")
            usuario = buscar_usuario_por_cpf(banco, cpf)
            if usuario:
                while True:
                    numero_conta = int(input("Digite o número da nova conta corrente (7 dígitos): "))
                    if len(str(numero_conta)) == 7: # verifica se a conta corrente tem 7 digitos
                        break
                    else:
                        print("O número da conta corrente deve ter exatamente 7 dígitos.")
                saldo_inicial = float(input(f"Digite o saldo inicial da conta corrente: "))
                banco.criar_conta_corrente(usuario, numero_conta, saldo_inicial)
                print(f"Conta corrente criada com sucesso para o usuário {usuario.nome}.")
            else:
                print(f"Usuário com CPF {cpf} não encontrado.")
# opção para criar conta poupança
        elif opcao == "3":
            cpf = input("Digite o CPF do usuário para criar a conta poupança: ")
            usuario = buscar_usuario_por_cpf(banco, cpf)
            if usuario:
                # loop
                while True:
                    numero_conta = int(input("Digite o número da nova conta poupança (4 dígitos): "))
                    if len(str(numero_conta)) == 4: # verifica se tem 4 digitos
                        break
                    else:
                        print("O número da conta poupança deve ter exatamente 4 dígitos.")
                saldo_inicial = float(input("Digite o saldo inicial da conta poupança: "))
                banco.criar_conta_poupanca(usuario, numero_conta, saldo_inicial)
                print(f"Conta poupança criada com sucesso para o usuário {usuario.nome}.")
            else:
                print(f"Usuário com CPF {cpf} não encontrado.")
# opção para criar conta de credito especial
        elif opcao == "4":
            cpf = input("Digite o CPF do usuário para criar a conta de crédito especial: ")
            usuario = buscar_usuario_por_cpf(banco, cpf)
            if usuario:
                while True:
                    numero_conta = int(input("Digite o número da nova conta de crédito especial (4 dígitos): "))
                    if len(str(numero_conta)) == 4:
                        break
                    else:
                        print("O número da conta de crédito especial deve ter exatamente 4 dígitos.")
                saldo_inicial = float(input("Digite o saldo inicial da conta de crédito especial: "))
                banco.criar_credito_especial(usuario, numero_conta, saldo_inicial)
                print(f"Conta de crédito especial criada com sucesso para o usuário {usuario.nome}.")
            else:
                print(f"Usuário com CPF {cpf} não encontrado.")
# opção listar usuários
        elif opcao == "5":
            banco.listar_usuarios()
# opção listar as contas registradas
        elif opcao == "6":
            cpf = input("Digite o CPF do usuário para listar suas contas: ")
            usuario = buscar_usuario_por_cpf(banco, cpf)
            if usuario:
                contas = usuario.listar_contas()
                if contas['corrente']:
                    print(f"Conta Corrente: {contas['corrente'].get_numero_conta()}")
                if contas['poupanca']:
                    print(f"Conta Poupança: {contas['poupanca'].get_numero_conta()}")
                if contas['credito_especial']:
                    print(f"Conta Crédito Especial: {contas['credito_especial'].get_numero_conta()}")
            else:
                print(f"Usuário com CPF {cpf} não encontrado.")
# opção do menu de operações bancárias
        elif opcao == "7":
            cpf = input("Digite o CPF do usuário para realizar operações bancárias: ")
            usuario = buscar_usuario_por_cpf(banco, cpf)
            if usuario:
                menu_operacoes = """
                **************** OPERAÇÕES BANCÁRIAS ****************
                1- Depósito
                2- Saque
                3- Transferência
                4- Imprimir Extrato
                0- Voltar
                *****************************************************
                """
                while True:# loop
                    print(f"\nOperações bancárias para o usuário {usuario.nome} ({usuario.cpf}):")
                    opcao_operacoes = input(menu_operacoes)
                    # tipo de conta - corrente, poupança, credito
                    if opcao_operacoes == "1":
                        tipo_conta = input("Digite o tipo de conta (corrente, poupanca, credito_especial): ")
                        conta = usuario.contas[tipo_conta]
                        if conta: # armazena valor do deposito
                            valor_deposito = float(input("Digite o valor a ser depositado: "))
                            conta.depositar(valor_deposito)
                        else:
                            print(f"Usuário {usuario.nome} não possui uma conta {tipo_conta}.")

                    elif opcao_operacoes == "2": # recebe do usuário tipo de conta
                        tipo_conta = input("Digite o tipo de conta (corrente, poupanca, credito_especial): ")
                        conta = usuario.contas[tipo_conta]
                        if conta: # armazena valor a ser sacado
                            valor_saque = float(input("Digite o valor a ser sacado: "))
                            if banco.verificar_limite_saques(conta): # verificar limite de saques
                                conta.sacar(valor_saque) # valor do saque
                        else:
                            print(f"Usuário {usuario.nome} não possui uma conta {tipo_conta}.")
                    # opção de transferências
                    elif opcao_operacoes == "3":
                        tipo_conta_origem = input("Digite o tipo de conta de origem (corrente, poupanca, credito_especial): ")
                        conta_origem = usuario.contas[tipo_conta_origem]
                        if conta_origem:
                            tipo_conta_destino = input("Digite o tipo de conta de destino (corrente, poupanca, credito_especial): ")
                            conta_destino = usuario.contas[tipo_conta_destino]
                            if conta_destino:
                                valor_transferencia = float(input("Digite o valor a ser transferido: "))
                                if conta_origem.get_saldo() >= valor_transferencia:
                                    conta_origem.transferir(valor_transferencia, conta_destino)
                                else:
                                    print("Saldo insuficiente na conta de origem.")
                            else:
                                print(f"Usuário {usuario.nome} não possui uma conta {tipo_conta_destino} de destino.")
                        else:
                            print(f"Usuário {usuario.nome} não possui uma conta {tipo_conta_origem} de origem.")
                    # extrato - da operações bancárias
                    elif opcao_operacoes == "4":
                        tipo_conta = input("Digite o tipo de conta (corrente, poupanca, credito_especial): ")
                        conta = usuario.contas[tipo_conta]
                        if conta:
                            conta.imprimir_extrato()
                        else:
                            print(f"Usuário {usuario.nome} não possui uma conta {tipo_conta}.")
                    # 0 para voltar
                    elif opcao_operacoes == "0":
                        break

                    else:
                        print("Opção inválida. Tente novamente.")

            else:
                print(f"Usuário com CPF {cpf} não encontrado.")
        # 0 para sair
        elif opcao == "0":
            print("Saindo do sistema bancário. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

# função para buscar usuário
def buscar_usuario_por_cpf(banco, cpf):
    for usuario in banco.usuarios:
        if usuario.get_cpf() == cpf:
            return usuario
    return None


if __name__ == "__main__": # chamando a string name com o metedo main
    main()
    breakpoint # breakpoin - ponto de interrupção
