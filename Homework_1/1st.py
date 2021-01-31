word = input("Введите слово или число: ")
answer_type = input("Это число? да/нет ")
if answer_type == "да":
    word = int(word)
    tip = "число"
    kvad = word**2
    answer = f"Введено число {word} Квадрат числа равен {kvad} Тип переменной {tip} "
    print("введено число: ", answer)
else:
    tip = "строка"
    revers = ''.join(reversed(word))
    answer = f"Введено слово {word}. Слово наоборот: {revers} Тип переменной {tip} "
    print(answer)
k = input("press close to exit")
