a = int(input("введите целое положительное число: "))
max=a%10
while a>0:
    a = a // 10
    if (a%10)<=max:
        continue
    else:
        max = a%10
print("максимальное число равно ", max)
k = input("press close to exit")






