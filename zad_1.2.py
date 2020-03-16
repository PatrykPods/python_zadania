dzien_oddania = int(input("podaj dzien tygodnia w ktorym oddales buty:"))
czas_naprawy = int(input("jaki jest czas naprawy?:"))

dzien_odbioru = dzien_oddania + czas_naprawy % 7

if dzien_odbioru == 1:
    print("buty mozesz odebrac w poniedzialek")
if dzien_odbioru == 2:
    print("buty mozesz odebrac we wtorek")
if dzien_odbioru == 3:
    print("buty mozesz odebrac w srode")
if dzien_odbioru == 4:
    print("buty mozesz odebrac w czwartek")
if dzien_odbioru == 5:
    print("buty mozesz odebrac w piatek")
if dzien_odbioru == 6:
    print("buty mozesz odebrac w sobote")
if dzien_odbioru == 7:
    print("buty mozesz odebrac w niedziele")