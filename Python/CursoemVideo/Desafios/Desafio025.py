n = str(input("Qual o seu nome completo? ")).strip()

s = ("SILVA" in n.upper())

'''
OU
 
s = ("silva" in n.lower())

'''

print("O seu nome é: {}" .format(n))

print("Ele possui Silva no nome? R: {}" .format(s))