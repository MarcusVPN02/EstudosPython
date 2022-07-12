vel = int(input("Qual a velocidade do carro? R: ").strip())

d = vel - 80

c = (vel - 80) * 7

if vel > 80:
    print("A velocidade do seu carro é de {}Km/h." .format(vel))
    print("O seu carro está {}km acima do limite de velocidade." .format(d))
    print("Você vai receber uma multa de R${},00" .format(c))
    print("Dirija com cuidado.")

else:
    print("A velocidade do seu carro é de {}Km/h." .format(vel))
    print("Dirija com segurança.")