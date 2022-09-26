import math


num = float(input("Digite um número: "))

numint = math.floor(num)

print("O número {} tem a parte inteira {} ou com truncate {}." .format(num, numint, math.trunc(num)))