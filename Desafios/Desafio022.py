n = input("Qual o seu nome completo? ")

m = n.upper()

l = n.lower()

tam = len(n.strip())


d = n.split()


print("Nome: {}." .format(n))

print("Nome em maiúsculo: {}." .format(m))

print("Nome em minúsculo: {}." .format(l))

print("Quantas letras esse nome possui: {}" .format(tam))

print("Primeiro nome {} letras." .format(len(d [0])))
