# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) e 
# depois faça uma chamada à função para listar os números      

def seq():
    for x in range(0,21):
        print("Número %a" %(x))
        x += 1

seq()
