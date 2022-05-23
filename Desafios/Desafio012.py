precoProd = float(input("Coloque o preço do produto: R$ "))

desc = (precoProd * 95) / 100

print("O produto tinha este valor: R$ {:.2f}." .format(precoProd))

print("O preço do produto com 5% de desconto é: {:.2f}" .format(desc))