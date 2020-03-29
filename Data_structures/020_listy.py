list = []
while len(list) < 10:
    number = int(input("podaj liczbe:"))
    list.append(number)

average = sum(list) / len(list)

print(f"srednia liczb z listy to {average:.2f}")


