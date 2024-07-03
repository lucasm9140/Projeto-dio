# Aluno: Lucas matheus
# Curso: Bootcamp Python & IA
# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
# TODO: Crie um loop para solicita os itens ao usuário:
# TODO: Solicite o item e armazena na variável "item":
# TODO: Adicione o item à lista "itens":
def main():
    # Cria uma lista vazia para armazenar os equipamentos
    itens = []
    # Loop para solicitar ao usuário inserir até três equipamentos
    for i in range(3):
        # Solicita o item ao usuário
        item = input()
        # Adiciona o item à lista de itens
        itens.append(item)
    # Exibe a lista de itens formatada
    print("\nLista de Equipamentos:")
    for item in itens:
        print(f"- {item}")
if __name__ == "__main__":
    main()
