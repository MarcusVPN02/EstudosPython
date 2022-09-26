# Exercício 10 - Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. Use um placeholder na 
# sua instrução de impressão

# “É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a 
# vantagem de existir.” (Machado de Assis)

f = ("É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir.")

contador = 0

for i in f:
    if i == "r":
        contador += 1

print("A quantidade da letra R é igual a: %a" %(contador))