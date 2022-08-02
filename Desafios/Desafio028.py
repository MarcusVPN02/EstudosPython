import random
from time import sleep

print("-=-" * 20)

n = int(input("Digite um número entre 0 e 5: ").strip())

print("-=-" * 20)

a = random.randint(0,5)

print("Processando...")

sleep(2)

if n == a:
    print("Você ganhou!!!")
    print("O número pensado era: {}" .format(a))
else:
    print("Você falhou!!!")
    print("O número pensado era: {}" .format(a))
