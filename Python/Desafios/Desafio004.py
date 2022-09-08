d = (input("Digite algo: "))


print("O tipo deste item é {}" .format(type(d)))

print("É alfanumérico?", d.isalnum())

print("É alfabético?", d.isalpha())

print("Têm letras maiúsculas? {}" .format(d.isupper()))

print("Têm letras minùsculas? {}" .format(d.islower()))

print("Tem capitalização? {}" .format(d.istitle()))
