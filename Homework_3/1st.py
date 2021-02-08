def calc(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Деление на 0")
        return
    return result

print("a/b= ", calc(int(input("Введите число а: ")), int(input("Введите число b: "))))
