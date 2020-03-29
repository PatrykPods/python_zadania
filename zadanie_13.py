min_x = None
max_x = None

while True:
    liczba = input("podaj liczbe:")
    if liczba == "x":
        break
    liczba = float(liczba)
    if min_x is None or liczba < min_x:
        min_x = liczba
    if max_x is None or liczba > max_x:
        max_x = liczba

print(f"wartosc max: {max_x}")
print(f"wartosc min: {min_x}")
