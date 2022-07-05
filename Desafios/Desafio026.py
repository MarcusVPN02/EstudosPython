f = str(input("Digite uma frase: ").upper().strip())

print("A letra A aparece {} vez(es)." .format(f.count("A")))

print("Primeira aparição: {}" .format(f.find("A") + 1))

print("Última aparição: {}" .format(f.rfind("A") + 1))
