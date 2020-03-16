wzrost = float(input("podaj wzrost w cm:"))
waga = float(input("podaj mase ciała w kg:"))

BMI = waga / (wzrost / 100) ** 2

if BMI < 16:
    print("jesteś wygłodzony!")
if BMI >= 16 and BMI <= 16.99:
    print("jestes wychudzony")
if BMI >= 17 and BMI <= 18.49:
    print("masz niedowage")
if BMI >= 18.5 and BMI <= 24.99:
    print("twoja waga jest odpowiednia")
if BMI >= 25 and BMI <= 29.99:
    print("masz nadwage")
if BMI >= 30:
    print("masz otylosc, przestan jesc w maku!")
