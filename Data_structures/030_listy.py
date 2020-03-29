dane = [39,-40, 32, 42, -2, -1, 12, 23, 23]

liczby_ujemne = []
liczby_dodatnie = []

for x in dane :
    if x >= 0:
        liczby_dodatnie.append(x)
    else:
        liczby_ujemne.append(x)

ilosc_liczb_ujemnych = len(liczby_ujemne)
ilosc_liczb_dodatnich = len(liczby_dodatnie)

print(f"liczby dodatnie: {ilosc_liczb_dodatnich}")
print(f"liczby ujemne: {ilosc_liczb_ujemnych}")

