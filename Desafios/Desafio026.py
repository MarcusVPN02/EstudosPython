f = input("Escreva uma frase: ")

print("Foram encontrados {} as na sua frase." .format(f.count("A")))

print("A primeira vez em que o A apareceu: {} posição." .format(f.find("A")))

print("Última aparição do A: {} posição." .format(f.find("A" in [:])))