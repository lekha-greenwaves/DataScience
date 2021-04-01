from functools import reduce
first_list=list(range(100,1001))
second_list = [el for el in first_list if el%2 == 0]
print(f'Новый список {second_list}')


print(f'Произведение равно: {reduce(lambda one,two: one*two ,second_list)} ')
