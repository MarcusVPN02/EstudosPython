nome = input("Digite o seu nome completo: ").strip()

maiu = nome.upper()

minu = nome.lower()

div = nome.split()

print("O seu nome é: {}" .format(nome))

print("Em maiúsculo fica: {}" .format(maiu))

print("Em minúsculo fica: {}" .format(minu))

print("O seu nome tem {} letras." .format(len(nome) - nome.count(" ")))

print("O seu primeiro nome é {} e ele tem {} letras." .format(div[0], len(div[0])))