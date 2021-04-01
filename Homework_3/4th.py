print("Первый способ")
def my_func(x, y):
    result=x**y
    return result
print("Результат по 1 способу равен: ", my_func(int(input("Введите число х: ")),
                                                int(input("Введите число y: ")) ))
print("Второй способ")
def my_func2(a, b):
    c=1
    d=1
    while c<=b:
        c=c+1
        d=d*a
    result_2=d
    return result_2
print("Результат по 2 способу равен: ", my_func2(int(input("Введите число a: ")),
                                                int(input("Введите число b: ")) ))