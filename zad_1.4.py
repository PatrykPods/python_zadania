wiek = int(input("podaj swoj wiek:"))
ilosc_nocy = int(input("podaj ilosc nocy:"))

if wiek < 18:
    koszt = ilosc_nocy * 100
    print(f"za pobyt zaplacisz {koszt} PLN")
if wiek >= 18 and wiek < 65 and ilosc_nocy == 1:
    print("za pobyt zaplacisz 200 PLN")
if wiek >= 18 and wiek < 65 and ilosc_nocy >= 2 and ilosc_nocy < 5:
    koszt = ilosc_nocy * 180
    print(f"za pobyt zaplacisz {koszt} PLN")
if wiek >= 18 and wiek < 65 and ilosc_nocy >= 5:
    koszt = ilosc_nocy * 150
    print(f"za pobyt zaplacisz {koszt} PLN")

if wiek >= 65 and ilosc_nocy == 1:
    print("za pobyt zaplacisz 180 PLN")
if wiek >= 65 and ilosc_nocy >= 2 and ilosc_nocy < 5:
    koszt = (ilosc_nocy * 180)*0.9
    print(f"za pobyt zaplacisz {koszt} PLN")
if wiek >= 65 and ilosc_nocy >= 5:
    koszt = (ilosc_nocy * 150)*0.9
    print(f"za pobyt zaplacisz {koszt} PLN")


