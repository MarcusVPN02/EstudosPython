d = int(input("Por quantos dias o carro foi alugado? "))

km = float(input("Quantos quilômetros você percorreu? "))

p = (d * 60) + (km * 0.15)

print("O preço a pagar pelo aluguel é: R$ {:.2f} " .format(p))