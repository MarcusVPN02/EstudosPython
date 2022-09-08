import math

num = float(input("Digite um valor: "))

s = math.sin(math.radians(num))

c = math.cos(math.radians(num))

t = math.tan(math.radians(num))

print("O seno de {} vale {:.2f}." .format(num, s))

print("O cosseno de {} vale {:.2f}." .format(num, c))

print("A tangente de {} vale {:.2f}." .format(num, t))