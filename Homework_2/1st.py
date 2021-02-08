chislo = list(map(int, input("введите несколько чисел ").split(" ")))
slovo = input("Введите несколько слов ")
slovo = slovo.split(" ")
my_list = chislo+slovo
print(chislo)
print(slovo)
print(chislo+slovo)
print(f"тип первого элемента {type(my_list[0])} тип последнего элемента {type(my_list[-1])}")

