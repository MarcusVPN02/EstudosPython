# nome = input("Qual o seu nome? ")

# print("Prazer em te conhecer {:x^20}!" .format(nome))

n1 = int(input("Digite um valor: "))

n2 = int(input("Digite outro valor: "))

s = n1 + n2

m = n1 * n2

d = n1 / n2

di = n1 // n2

e = n1 ** n2



print("A soma de {} e de {} vale {}, o produto vale {},\n a divisão vale {}, "
      "a divisão inteira\n vale {} e a exponenciação vale {}."
      .format(n1, n2, n1+n2, m, d, di, e))
