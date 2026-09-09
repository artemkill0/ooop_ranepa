class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color

    def draw(self):
        print("Рисуется фигура")

class Line(Figure):
    def draw(self):
        print("Рисуется линия")

class Rect(Figure):
    def draw(self):
        print("Рисуется прямоугольник")

class Ellipse(Figure):
    def draw(self):
        print("Рисуется эллипс")

class Triangle(Figure):
    def draw(self):
        print("Рисуется треугольник")

figures = [
    Line([(0,0), (10,10)], 1, "black"),
    Rect([(0,0), (10,10)], 2, "red"),
    Ellipse([(5,5), (15,15)], 3, "blue")
]

for f in figures:
    f.draw()

figures.append(Triangle([(0,0), (10,0), (5,10)], 1, "green"))

for f in figures:
    f.draw()