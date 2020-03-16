a = float(input("podaj dlugosc boku a w cm:"))
b = float(input("podaj dlugosc boku b w cm:"))
c = float(input("podaj dlugosc boku c w cm:"))

if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    import math
    pole = math.sqrt(p * (p - a) * (p - b) * (p - c))

    print(f"odcinki o tych długościach mogą utworzyć trójkąt o polu {pole:.2f} cm^2") #jak zrobic indeks gorny???
else:
    print("odcinki o tych dlugosciach nie moga utworzyc trojkata")

