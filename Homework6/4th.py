class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        return f'{self.name} поехал'

    def stop(self):
        return f'{self.name} остановился'

    def turn_right(self):
        return f'{self.name} повернул направо'

    def turn_left(self):
        return f'{self.name} повернул налево'

    def show_speed(self):
        return f'Скорость {self.name}  {self.speed} кмч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name}  {self.speed} кмч')

        if self.speed > 40:
            return f'Скорость {self.name} превышена'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name} {self.speed} кмч')

        if self.speed > 60:
            return f'Скорость {self.name} превышена'



class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} - полиция'
        else:
            return f'{self.name} - не полиция'


F = SportCar(150, 'Белый', 'Ferrari', False)
L = TownCar(60, 'Зеленый', 'Lada', False)
Z = WorkCar(70, 'Красный', 'Жигули', False)
B = PoliceCar(130, 'Черный', 'BMW', True)
print(F.turn_left())
print(f'{L.turn_right()}')
print(f'{F.stop()}')
print(f'{L.show_speed()}')
print(f'{L.name}  {L.color}')
print(f'{F.name} это полиция? {F.is_police}')
print(f'{L.name} это полиция? {L.is_police}')
print(L.show_speed())
print(Z.show_speed())
print(B.police())
print(B.show_speed())