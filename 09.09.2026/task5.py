class Point:
    def __init__(self, x, y, color="black"):
        self.x = x
        self.y = y
        self.color = color

points = [
    Point(1, 2),
    Point(3, 4, "red"),
    Point(5, 6, "blue")
]

for p in points:
    print(p.x, p.y, p.color)