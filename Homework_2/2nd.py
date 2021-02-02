spisok = list(map(int, input("введите несколько чисел ").split(" ")))
for el in range(1, len(spisok), 2):
    spisok[el - 1], spisok[el] = spisok[el], spisok[el - 1]
print(spisok)

