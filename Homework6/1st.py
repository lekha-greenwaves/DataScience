from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def switch(self):
        print(f'Цвет светофора ')
        i = 0
        while i < 3:
            print(f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(2)
            i += 1


a = TrafficLight()
a.switch()
