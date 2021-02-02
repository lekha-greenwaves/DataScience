slovo = input("Введите несколько слов ")
slovo = slovo.split(" ")
for num, el in enumerate(slovo):
    if len(el)<10:
        print (num+1,el)
    else:
        print (num+1,el[0:10])

    

