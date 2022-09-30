# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma 
# lista

t = (1,2,3,4)

l = []

for i in t:
    res = i * 2
    l.append(res)

print(l)