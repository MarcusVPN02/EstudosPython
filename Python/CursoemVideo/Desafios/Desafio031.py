d = int(input("Qual a distância da sua viagem em Km? R: ").strip())

cm = d * 0.5

cn = d * 0.45

if d <= 200:
    print("A distância da sua viagem: {:.2f}" .format(d))
    print("O custo da sua viagem será de R${:.2f}" .format(cm))
else: 
    print("A distância da sua viagem: {:.2f}" .format(d))
    print("O custo da sua viagem será de R${:.2f}" .format(cn))
    
    '''OU preço = d * 0.50 if d <= 200 else d * 0.45
