# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista

def func(adiciona):
    print(adiciona.append(5))
    print(adiciona.append(6))

lista = [1,2,3,4]

func(lista)

print(lista)