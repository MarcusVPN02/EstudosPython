p = int(input("Digite um número: "))
s = int(input("Digite um número: "))
t = int(input("Digite um número: "))

menor = p 

if s < p and s < t:
    menor = s
    
if t < p and t < s:
    menor = t
    
maior = p 

if s > p and s > t:
    maior = s
if t > p and t > s: 
    maior = t
print("O menor número é: {}" .format(menor))

print("O maior número é: {}" .format(maior))
