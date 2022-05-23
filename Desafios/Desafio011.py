l = float(input("Digite a largura da parede: "))

h = float(input("Digite a altura da parede: "))

area = h * l

TintaLata = area / 2

print("A sua parede tema dimensão de {} por {} e a sua área é de {}m²." .format(l, h, area))

print("A quantidade de tinta necessária é: {} litros" .format(TintaLata))