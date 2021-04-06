from math import factorial
n=int(input("Введите количество факториалов: "))
def fact(n):
    for el in range(1,n+1):
        yield el

for el in fact(n):
    znach_fact=factorial(el)
    print (f"Факториал числа {el} равен {znach_fact}")

