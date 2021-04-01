numb = int(input("Введите число "))
spisok = [10,7,5]
for el in spisok:
    if el > numb:
        continue
    else:
        spisok.insert(spisok.index(el), numb)
        print(spisok)
        break

