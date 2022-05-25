import math

graus = int(input("Coloque um valor de graus: "))

seno = math.sin(graus)

cos = math.cos(graus)

tang = math.tan(graus)

print("O valor digitado em graus é: {}°." .format(graus))

print("O seno vale: {:.3f}." .format(seno))

print("O valor do cosseno é:{:.3f}." .format(cos))

print("O valor da tangente é: {:.3f}." .format(tang))
