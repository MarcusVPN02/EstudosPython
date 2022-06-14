num = int(input("Digite um valor entre 0 a 9999: "))


# % 10 vai pegaro que está atrás da vírgula

uni = num // 1 % 10

dez = num // 10 % 10

cen = num // 100 % 10

mil = num // 1000 % 10

print("Você digitou {}" .format(num))

print("O valor da unidade é: {}."  .format(uni))

print("O valor da dezena é: {}." .format(dez))

print("O valor da centena é: {}." .format(cen))

print("O valor da unidade de milhar: {}." .format(mil))