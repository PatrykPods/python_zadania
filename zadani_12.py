x = 7
temp = 0
while x > 0:
    temperature = float(input("podaj temperaturę w kolejnych dniach tygodnia zaczynając od poniedziałku:"))
    temp += temperature
    x -= 1

average = temp / 7
print(f"srednia temperatura to:{average}")




