import unittest
from circles import Circle


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.circle1 = Circle(0, 0, 5)
        self.circle2 = Circle(3, 4, 2)
        self.circle3 = Circle(10, 5, 3)

    def test_repr(self):
        self.assertEqual(repr(self.circle1), "Circle(0, 0, 5)")

    def test_eq(self):
        self.assertEqual(self.circle1, Circle(0, 0, 5))
        self.assertNotEqual(self.circle1, self.circle2)

    def test_ne(self):
        self.assertNotEqual(self.circle1, self.circle2)
        self.assertNotEqual(self.circle1, self.circle3)

    def test_area(self):
        self.assertAlmostEqual(self.circle1.area(), 78.54, places=2)

    def test_move(self):
        self.circle1.move(2, 3)
        self.assertEqual(repr(self.circle1), "Circle(2, 3, 5)")

    def test_cover(self):
        covered_circle = self.circle1.cover(self.circle2)
        self.assertEqual(repr(covered_circle), "Circle(1.5, 2.0, 5.0)")


if __name__ == '__main__':
    unittest.main()
