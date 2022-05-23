num = float(input("Digite um valor em metros: "))

nkm = (num / 1000)
nhm = (num / 100)
ndam = (num / 10)
ndm = (num * 10)
ncm = (num * 100)
nmm = (num * 1000)

print("O valor {}m  em centímetros é {}cm." .format(num, ncm))

print("{}km" .format(nkm))
print("{}nhm" .format(nhm))
print("{}dam" .format(ndam))
print("{}m" .format(num))
print("{}dm" .format(ndm))
print("{}ncm" .format(ncm))
print("{}nmm" .format(nmm))
