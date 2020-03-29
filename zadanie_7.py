liczba = int(input("podaj liczbe:"))

print(f"""
liczba jest podzielna przez 2 oraz 3, jest wieksza od 10 lub jest to liczba 7: {liczba % 2 == 0 and liczba % 3 == 0 
and liczba > 10 or liczba == 7} 
""")
