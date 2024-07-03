#Autor: Lucas matheus
#Curso: Dio - Bootcamp Python & IA

# importa biblioteca(modulo re)
import re
# Função validar numero.
def validar_numero_telefone(numero):
    # Expressão regular para validar o formato (XX) 9XXXX-XXXX
    regex = r'^\(\d{2}\) 9\d{4}-\d{4}$'
    
    # Verifica se a string corresponde ao padrão
    if re.match(regex, numero):
        return print("Número de telefone válido.")#retorna mensagem na tela
    else:
        return print("Número de telefone inválido.")# retorna mensagem na tela

# Solicita a entrada do usuário
numero_telefone = input()

# Valida o número de telefone
resultado = validar_numero_telefone(numero_telefone)