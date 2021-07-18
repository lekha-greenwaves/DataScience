first_list=list(range(20,240))
second_list = [el for el in first_list if el%21  == 0 or el%20  == 0 ]
print(f'Новый список {second_list}')