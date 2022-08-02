import random

t = int(input("Digite um valor entre 0 a 5 e vejamos se \nvocê pensou no mesmo número que o computador:  ").strip())

x = random.randint(0,5)

if t == x:
    print("Meus parabéns!!")
    print("Este é o número que você escolheu: {}" .format(t))
    print("Este é o número que o computador pensou: {}" .format(x))

else: 
    print("Que pena, voxê falhou.")
    print("O seu número: {}" .format(t))
    print("O número do computador: {}" .format(x))
