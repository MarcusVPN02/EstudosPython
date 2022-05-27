'''import math

cato = float(input("Digite o valor do cateto oposto: "))

cata = float(input("Digite o valor do cateoto adjacente: "))

catoa = (cato ** 2) + (cata ** 2)

hipo = catoa ** (1/2)

print("O cateto oposto vale {}." .format(cato))

print("O cateto adjacente vale {}." .format(cata))

print("A hipotenusa vale {}." .format(hipo))'''

import math 

co = float(input("Digite o valor do cateto oposto: "))

ca = float(input("Digite o valor do cateoto adjacente: "))

h = math.hypot(co, ca)

print("A soma dos catetos {} e {} vale {:.2f}." .format(co, ca, h))