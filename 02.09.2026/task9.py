import math

class Figure:
    def __init__(self, coords, width, color):
        self._coords = coords
        self._width = width
        self._color = color
    
    def get_coords(self):
        return self._coords
    
    def set_coords(self, coords):
        self._coords = coords
    
    def calculate_area(self):
        return 0

class Circle(Figure):
    def __init__(self, coords, width, color, radius):
        super().__init__(coords, width, color)
        self._radius = radius
    
    def calculate_area(self):
        return math.pi * self._radius ** 2

class Square(Figure):
    def __init__(self, coords, width, color, side):
        super().__init__(coords, width, color)
        self._side = side
    
    def calculate_area(self):
        return self._side ** 2

figures = [
    Circle((0, 0), 2, "красный", 5),
    Square((5, 5), 4, "синий", 4),
    Circle((10, 10), 3, "зелёный", 3),
    Square((15, 15), 5, "жёлтый", 6),
    Circle((20, 20), 2, "фиолетовый", 7)
]

total_area = 0
for figure in figures:
    area = figure.calculate_area()
    total_area += area
    print(f"Площадь фигуры: {area:.2f}")

print(f"\nОбщая площадь всех фигур: {total_area:.2f}")