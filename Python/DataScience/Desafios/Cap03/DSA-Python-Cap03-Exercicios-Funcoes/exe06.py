# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local
total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2; 
    print ("Dentro da função o total é: ", total)
    return total;

# total = 0 é uma variável global com valor de 0

soma( 10, 20 );
print ("Fora da função o total é: ", total)

# Enquanto total dentro de soma é local. Obs: Melhor mudar o nome desta 
# variável para não gerar confusão 