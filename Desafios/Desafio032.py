a = int(input("Em que ano você está? R: "))

b = a % 4

d = a % 100

if b == 0:
    print("O digitado foi: {}" .format(a))
    print("O ano é bissexto.")

else: 
    print("O ano não é bissexto.")
     