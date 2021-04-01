
first_list = [2, 3, 2, 3, 23, 1, 44, 44, 3, 2, 10, 8, 4, 11, 26, 27, 32, 48]
second_list = [el for el in first_list if first_list.count(el) ==1 ]
print(f'Исходный список {first_list}')
print(f'Новый список {second_list}')