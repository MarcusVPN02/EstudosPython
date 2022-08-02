a = int(input("Qua ano você deseja analisar? R: ").strip())


if a % 4 == 0 and a % 100 != 0: 
    
    print("O ano {} é bissexto." .format(a))
    
else:
    print("O ano {} não é bissexto." .format(a))
   
     
