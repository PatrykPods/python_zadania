a = float(input("podaj dlugosc opakowania:"))
b = float(input("podaj szerokosc opakowania:"))
h = float(input("podaj wysokosc opakowania:"))

objetosc = (a * b) * h

print(f""" 
objetosc opakowania to: {objetosc} cm3
czy jest ona wieksza od 1 litra?: {objetosc >= 1000}
""")
