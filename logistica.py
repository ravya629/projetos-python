# logistica.py

def calcular_frete(peso):
    if peso <= 20:
        valor = peso * 10
    else:
        valor = peso * 15

    return valor


# Entrada de dados
peso_carga = float(input("Digite o peso da carga (kg): "))

# Cálculo do frete
frete = calcular_frete(peso_carga)

# Saída
print(f"Valor final do frete: R$ {frete:.2f}")