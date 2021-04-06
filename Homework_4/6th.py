
from itertools import count
start=int(input("Введите стартовое число: "))
for el in count(start):
    if el > 1000:
        break
    else:
        print(el)

from itertools import cycle
start_list=input("Введите набор букв: ")
start_list=start_list.split(" ")
c=0
for el in cycle(start_list):
    if c > 1000:
        break
    print(el)
    c+=1
