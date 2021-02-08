spisok= 0
numbers = 0
summa = 0
print("Для выхода из программы введите ! ")
while True:
    spisok = input("введите несколько чисел: ")
    if spisok == "!":
        break
    else:
        numbers = map(int, spisok.split(" "))
        summa= sum(numbers)+ summa
        print(f"Сумма чисел равна {summa}")
print("расчет окончен")
