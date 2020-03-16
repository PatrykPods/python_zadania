cena = float(input("podaj cene za kg. ziemniakow:"))
ilosc = float(input("ile kg. ziemniakow chcesz kupic?:"))
koszt = cena * ilosc

ilosc_bananow = float(input("ile kg. bananow chcesz kupic?:"))
cena_bananow = float(input("podaj cene za kg. bananow:"))
koszt_bananow = ilosc_bananow * cena_bananow


laczny_koszt = koszt_bananow + koszt

print(f"laczny_koszt za {ilosc:.2f}kg ziemniakow oraz {ilosc_bananow:.2f}kg bananow wynosi {laczny_koszt:.2f}PLN")

