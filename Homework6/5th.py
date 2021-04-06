class Stationery:
    title = "Канцелярия"
    print(f'{title}')
    def draw(self):
        print('Запуск отрисовки')
class Pen(Stationery):
    title = 'ручка'
    def draw(self):
        print(f'Рисование {self.title}й')
class Pencil(Stationery):
    title = 'карандаш'
    def draw(self):
        print(f'Рисование {self.title}ом')
class Handle(Stationery):
    title = 'маркер'
    def draw(self):
        print(f'Рисование {self.title}ом')
stationery=Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()
stationery.draw()
pen.draw()
pencil.draw()
handle.draw()