def recomendar_plano(consumo_medio):
    if consumo_medio <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    elif consumo_medio > 10 and consumo_medio <= 20:
        return "Plano Prata Fibra - 100Mbps"
    elif consumo_medio > 20:
        return "Plano Premium Fibra - 300Mbps"

# Solicita a entrada do usuário
consumo_medio = float(input())

# Chama a função e exibe a recomendação de plano
plano_recomendado = recomendar_plano(consumo_medio)
print(plano_recomendado)
