towar = input("co chcesz kupic?")
cena = float(input("podaj cene towaru:"))
ilosc = float(input("podaj ilosc jaka chcesz kupic:"))

koszt = cena * ilosc

print(f"za {towar} zaplacisz {koszt:.2f} PLN")

