from circles import Circle
from point import Point
import pytest


def test_circle_top():
    circle = Circle(0, 0, 5)
    assert circle.top == 5


def test_circle_left():
    circle = Circle(0, 0, 5)
    assert circle.left == -5


def test_circle_bottom():
    circle = Circle(0, 0, 5)
    assert circle.bottom == -5


def test_circle_right():
    circle = Circle(0, 0, 5)
    assert circle.right == 5


def test_circle_width():
    circle = Circle(0, 0, 5)
    assert circle.width == 10


def test_circle_height():
    circle = Circle(0, 0, 5)
    assert circle.height == 10


def test_circle_topleft():
    circle = Circle(0, 0, 5)
    assert circle.topleft == Point(-5, 5)


def test_circle_bottomleft():
    circle = Circle(0, 0, 5)
    assert circle.bottomleft == Point(-5, -5)


def test_circle_topright():
    circle = Circle(0, 0, 5)
    assert circle.topright == Point(5, 5)


def test_circle_bottomright():
    circle = Circle(0, 0, 5)
    assert circle.bottomright == Point(5, -5)


def test_circle_creation():
    circle = Circle(1, 2, 7)
    assert circle.pt == Point(1, 2)
    assert circle.radius == 7


def test_circle_area():
    circle = Circle(1, 2, 7)
    assert circle.area() == pytest.approx(153.94, rel=1e-2)


def test_circle_move():
    circle = Circle(1, 2, 7)
    circle.move(3, 4)
    assert circle.pt == Point(4, 6)


def test_circle_cover():
    circle1 = Circle(0, 0, 5)
    circle2 = Circle(0, 0, 2)
    circle3 = Circle(0, 0, 18)

    assert circle1.cover(circle2) == circle1
    assert circle1.cover(circle3) == circle3
    assert circle2.cover(circle3) == circle3


def test_circle_from_points():
    point1 = Point(1, 0)
    point2 = Point(0, 1)
    point3 = Point(0, 0)
    circle = Circle.from_points((point1, point2, point3))

    assert circle.pt == Point(0.5, 0.5)
    assert circle.radius == pytest.approx(0.7, rel=0.1)
