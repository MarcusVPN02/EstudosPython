num = int(input("Digite um valor entre 0 a 9999: "))

'''n = str(num) NÃO É A MELHOR MANEIRA'''

u = num // 1 % 10  #Pega o resto da divisão por 10

d = num // 10 % 10

c = num // 100 % 10

m = num // 1000 % 10

print("O número é {}" .format(num))

print("Unidade: {}" .format(u))

print("Dezena: {}" .format(d))

print("Centena: {}" .format(c))

print("Milhar: {}" .format(m))

