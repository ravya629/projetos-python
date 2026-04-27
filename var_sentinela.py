# Exemplo de uso da variável sentinela
while true:
    comando = input("digite um comando-para parar digite ´sair`")
if comando == "sair":
    break
print(f"executando:{comando}")