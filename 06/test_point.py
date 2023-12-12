import unittest
from point import Point


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.point1 = Point(1, 2)
        self.point2 = Point(3, 4)
        self.point3 = Point(1, 2)

    def test_str(self):
        self.assertEqual(str(self.point1), "(1, 2)")
        self.assertEqual(str(self.point2), "(3, 4)")

    def test_repr(self):
        self.assertEqual(repr(self.point1), "Point(1, 2)")
        self.assertEqual(repr(self.point2), "Point(3, 4)")

    def test_eq(self):
        self.assertEqual(self.point1, self.point3)
        self.assertNotEqual(self.point1, self.point2)

    def test_ne(self):
        self.assertNotEqual(self.point1, self.point2)
        self.assertEqual(self.point1, self.point3)

    def test_add(self):
        result = self.point1 + self.point2
        self.assertEqual(result, Point(4, 6))

    def test_sub(self):
        result = self.point2 - self.point1
        self.assertEqual(result, Point(2, 2))

    def test_mul(self):
        result = self.point1 * self.point2
        self.assertEqual(result, 11)

    def test_cross(self):
        result = self.point1.cross(self.point2)
        self.assertEqual(result, -2)

    def test_length(self):
        result = self.point1.length()
        self.assertEqual(result, 5 ** 0.5)

    def test_hash(self):
        hash_value = hash(self.point1)
        self.assertIsInstance(hash_value, int)


if __name__ == '__main__':
    unittest.main()
