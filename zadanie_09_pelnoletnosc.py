import datetime

current_year = datetime.datetime.now().year

rok_urodzenia = int(input("podaj date urodzenie:"))

wiek = current_year - rok_urodzenia

if wiek >= 18:
    print("jestes pelnoletni")
else:
    print("nie jestes pelnoletni")