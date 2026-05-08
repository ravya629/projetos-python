# Quiz em Python - Tema: Tecnologia

print("=== QUIZ DE TECNOLOGIA ===\n")

pontuacao = 0

# Pergunta 1
print("1) O que significa CPU?")
print("a) Central Process Unit")
print("b) Central Processing Unit")
print("c) Computer Personal Unit")

resposta = input("Digite a alternativa correta: ").lower()

if resposta == "b":
    print("✅ Você acertou!\n")
    pontuacao += 1
else:
    print("❌ Você errou! A resposta correta era: b\n")

# Pergunta 2
print("2) Qual destas linguagens é usada para desenvolvimento web?")
print("a) HTML")
print("b) Excel")
print("c) Windows")

resposta = input("Digite a alternativa correta: ").lower()

if resposta == "a":
    print("✅ Você acertou!\n")
    pontuacao += 1
else:
    print("❌ Você errou! A resposta correta era: a\n")

# Pergunta 3
print("3) Qual empresa criou o sistema operacional Android?")
print("a) Apple")
print("b) Microsoft")
print("c) Google")

resposta = input("Digite a alternativa correta: ").lower()

if resposta == "c":
    print("✅ Você acertou!\n")
    pontuacao += 1
else:
    print("❌ Você errou! A resposta correta era: c\n")

# Resultado final
print("=== RESULTADO FINAL ===")
print(f"Você acertou {pontuacao} de 3 questões.")

if pontuacao == 3:
    print("🏆 Excelente!")
elif pontuacao == 2:
    print("👍 Muito bom!")
elif pontuacao == 1:
    print("🙂 Você pode melhorar!")
else:
    print("📚 Estude mais e tente novamente!")

    # ravy dants da silva