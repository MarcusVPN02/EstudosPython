d = int(input("Qual a distância da viagem em quilômetros? R: ").strip())

l = d * 0.50

if d <= 200:
    print("A sua viagem possui uma distância de {}Km." .format(d))
    print("A sua passagem vai custar R${:.2f}" .format(l))
    print("Boa viagem!")

else: 
    print("A sua viagem possui {} de distância" .format(d))
    print("A sua viagem vai custar R${:.2f}" .format(d * 0.45))
    print("Boa viagem!")
