time = int(input("Введите время в секундах "))
hour = time // 3600
minute = time%3600 // 60
second = (time%3600)%60
text = f"Время {hour}:{minute}:{second}"
print(text)
k = input("press close to exit")
