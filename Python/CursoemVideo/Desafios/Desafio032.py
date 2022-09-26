from datetime import date

a = int(input("Qua ano você deseja analisar? Se deseja saber o ano atual, pressione 0. R: ").strip())

if a == 0: 
    a = date.today().year

if a % 4 == 0 and a % 100 != 0: 
    
    print("O ano {} é bissexto." .format(a))
    
else:
    print("O ano {} não é bissexto." .format(a))
