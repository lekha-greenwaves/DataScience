class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def weight(self):
        self.spec_weight = 25
        self.thickness = 5
        as_weight = self._length * self._width * self.spec_weight * self.thickness
        print(f'Масса асфальта: {as_weight}')

a = Road(20, 5)
a.weight()

