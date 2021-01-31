vir = int(input("введите сумму выручки за год: "))
izd = int(input("введите сумму издержек за год: "))
razn = vir - izd
if razn > 0:
    print(f"Прибыль составила: {razn} руб")
    rent=razn/vir
    print(f"Рентабельность составила: {rent} ")
    shtat = int(input("введите количество сотрудников: "))
    udel=razn/shtat
    print(f"Удельная выручка составила: {udel} руб/чел")
elif razn == 0:
    print("Фирма вышла в \"ноль\" ")
elif razn < 0:
    print(f"Убыток составил: {abs(razn)} руб")
k = input("press close to exit")

