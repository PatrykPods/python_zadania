cena_ziemniakow = float(input("podaj cene za kg. ziemniakow:"))
ilosc_ziemniakow = float(input("ile kg. ziemniakow chcesz kupic?:"))
koszt_ziemniakow = cena_ziemniakow * ilosc_ziemniakow

ilosc_bananow = float(input("ile kg. bananow chcesz kupic?:"))
cena_bananow = float(input("podaj cene za kg. bananow:"))
koszt_bananow = ilosc_bananow * cena_bananow


laczny_koszt = koszt_bananow + koszt_ziemniakow

print(f"laczny_koszt za {ilosc_ziemniakow:.2f}kg ziemniakow oraz {ilosc_bananow:.2f}kg bananow wynosi {laczny_koszt:.2f}PLN")

if koszt_bananow < koszt_ziemniakow:
    print("za ziemniaki zaplacimy wiecej niz za banany")
if koszt_bananow > koszt_ziemniakow:
    print("za banany zaplacimy wiecej niz za ziemniaki")
if koszt_bananow == koszt_ziemniakow:
    print("banany kosztują tyle samo co ziemniaki")