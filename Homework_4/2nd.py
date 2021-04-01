first_list = [4, 8, 15, 42, 23, 16]
second_list = [el for el in first_list if el>first_list[first_list.index(el)-1]]
print(f'Исходный список {first_list}')
print(f'Новый список {second_list}')