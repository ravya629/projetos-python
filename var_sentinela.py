# Exemplo de uso da variável sentinela
while True:
    comando = input("digite um comando para parar. digite 'sair'")
    if comando == "sair":
     break
print("executando: {comando}")