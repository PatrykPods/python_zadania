a = int(input("podaj dlugosc opakowania:"))
b = int(input("podaj szerokosc opakowania:"))
h = int(input("podaj wysokosc opakowania:"))

objetosc = (a * b) * h
print(f""" objetosc opakowania to: {objetosc} cm3
czy jest ona wieksza od 1 litra?: {objetosc >= 1000}
""")
