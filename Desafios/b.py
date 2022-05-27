ca = float(input("Digite o valor do cateto adjacente: "))

co = float(input("Digite o valor do cateto oposto: "))

h = ((ca ** 2) + (co ** 2)) ** (1/2)

print("Os valores são: {} e {}, hipotenusa vale {:.3f}." .format(ca, co, h))