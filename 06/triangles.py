from point import Point


class Triangle:
    """Klasa reprezentująca trójkąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):
        return "[(%s, %s), (%s, %s), (%s, %s)]" % (self.pt1.x, self.pt1.y, self.pt2.x,
                                                   self.pt2.y, self.pt3.x, self.pt3.y)

    def __repr__(self):
        return "Triangle(%s, %s, %s, %s, %s, %s)" % (self.pt1.x, self.pt1.y, self.pt2.x,
                                                     self.pt2.y, self.pt3.x, self.pt3.y)

    def __eq__(self, other):
        # Sprawdź, czy zbiory wierzchołków są takie same, niezależnie od kolejności
        return {self.pt1, self.pt2, self.pt3} == {other.pt1, other.pt2, other.pt3}

    def __ne__(self, other):
        return self != other

    def center(self):
        # Oblicza środek trójkąta jako średnią arytmetyczną współrzędnych
        x = (self.pt1.x + self.pt2.x + self.pt3.x) / 3
        y = (self.pt1.y + self.pt2.y + self.pt3.y) / 3
        return Point(x, y)

    def area(self):
        # Oblicza pola powierzchni za pomocą wzoru z determinatą macierzy
        return 0.5 * abs(
            self.pt1.x * (self.pt2.y - self.pt3.y) + self.pt2.x * (self.pt3.y - self.pt1.y) + self.pt3.x * (
                        self.pt1.y - self.pt2.y))

    def move(self, x, y):
        # Przesuń trójkąt o (x, y)
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y
        self.pt3.x += x
        self.pt3.y += y
