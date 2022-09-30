# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos

def arg(frase, *list): # * SIGNIFICA VÁRIOS ARGUMENTOS
    print(frase)

    for ele in list:
        print(ele)

arg("Teste")

arg(100,1,2)
