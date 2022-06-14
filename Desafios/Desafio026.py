f = str(input("Digite uma frase: ")).strip()

a = f.lower().count("a", 0, )

p = f.lower().lfind(a)

u = f.lower().rfind(a)

print("Você digitou: \n{}" .format(f))

print("A letra a apareceu {} vezes." .format(a))

print(p)

print(u)