# multiplas funçoes -- exercicios controle de qualidade --
def cabecalho():
    print("\n "+"=" *30)
    print("SISTEM DE QUALIDADE")
def verificar_status(peso):
    if peso >= 50 and peso <=100:
        return "Aprovada"
    else:
        return "Reprovada"
cabecalho()
peso_item = float(input("Digite o peso do item em gramos:"))
status = verificar_status(peso_item)
print(f"resultado da inspiração:{status}")
print("=" *30)