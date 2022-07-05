n = str(input("Nome completo: ").strip())

d = n.split()

print("Seu nome é {}." .format(n))

print("O seu primeiro nome é: {}" .format(d[0]))

print("O seu último nome é: {}". format(d[len(d) - 1]))
