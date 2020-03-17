wiek = int(input("ile masz lat?"))
ilosc_biletow = int(input("ile biletow chcesz kupic?"))

if wiek <= 6:
    print("bilety sa darmowe")
elif wiek >= 7 and wiek <= 17:
    koszt = ilosc_biletow * 2.28
    print(f"koszt biletow: {koszt:.2f} PLN")
elif wiek >= 18 and wiek <= 64:
    koszt = ilosc_biletow * 3.80
    print(f"koszt biletow: {koszt:.2f} PLN")
elif wiek >= 65:
    koszt = ilosc_biletow * 1.90
    print(f"koszt biletow: {koszt:.2f} PLN")
    