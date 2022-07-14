import math

l1 = float(input("Lado 1: ").strip())
l2 = float(input("Lado 2: ").strip())
l3 = float(input("Lado 3: ").strip())

s = (l1 * l1) + (l2 * l2)

r = math.sqrt(s)

h =  l3 * l3

rz = math.sqrt(h)

if r == rz:
    print("Posso fazer um triângulo")
    
else: 
    print("Não posso")
