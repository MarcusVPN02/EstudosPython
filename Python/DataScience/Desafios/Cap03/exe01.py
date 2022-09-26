# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"

ask = str(input("Que dia é hoje? R: ") .lower().strip())

if ask == "sabado" or "domingo":
    print("Hoje é dia de descanso")
else:
        print("Você precisa trabalhar!")