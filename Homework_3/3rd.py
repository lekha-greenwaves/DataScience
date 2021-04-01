def my_func(a,b,c):
    if a >= b and b >= c:
        return a + b
    elif a > b and a < c:
        return a + c
    else:
        return b + c
print("Сумма равна: ", my_func(int(input("Введите число а: ")),int(input("Введите число b: ")),int(input("Введите число c: "))))
