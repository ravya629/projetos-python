# ferramenta de conversão dólar x Real --
def converter(valor_dolar):
    taxa = 5.15
    valor_real = valor_dolar * taxa
    return valor_real
print("Conversor dólar x Real")
preco = float(input("Digite o preço do Produto em Dólar:"))
resultado = converter(preco)
print(f"O Valor em Reais é:{resultado:.2f}")