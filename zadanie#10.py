pierwsza_liczba = float(input("podaj pierwsza liczbe:"))
druga_liczba = float(input("podaj drugą liczbę:"))
działanie = input("jakie działanie chcesz wykonać?:")

if działanie == "*" :
    print(pierwsza_liczba * druga_liczba)
elif działanie == "/" :
    print(pierwsza_liczba / druga_liczba)
elif działanie == "-" :
    print(pierwsza_liczba - druga_liczba)
elif działanie == "+" :
    print(pierwsza_liczba + druga_liczba)
else:
    print("podałes nieprawidłowe działanie")
