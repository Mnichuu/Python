import unittest
from triangles import Triangle


class TestTriangle(unittest.TestCase):
    def test_str(self):
        tr = Triangle(0, 0, 1, 1, 2, 0)
        self.assertEqual(str(tr), "[(0, 0), (1, 1), (2, 0)]")

    def test_repr(self):
        tr = Triangle(0, 0, 1, 1, 2, 0)
        self.assertEqual(repr(tr), "Triangle(0, 0, 1, 1, 2, 0)")

    def test_eq(self):
        tr1 = Triangle(0, 0, 1, 1, 2, 0)
        tr2 = Triangle(1, 1, 2, 0, 0, 0)
        self.assertEqual(tr1, tr2)

    def test_ne(self):
        tr1 = Triangle(0, 0, 1, 1, 2, 0)
        tr2 = Triangle(0, 0, 1, 1, 2, 0)
        self.assertNotEqual(tr1, tr2)

    def test_center(self):
        tr = Triangle(0, 0, 1, 0, 0, 1)
        center = tr.center()
        self.assertEqual(center.x, 1 / 3)
        self.assertEqual(center.y, 1 / 3)

    def test_area(self):
        tr = Triangle(0, 0, 1, 0, 0, 1)
        self.assertEqual(tr.area(), 0.5)

    def test_move(self):
        tr = Triangle(0, 0, 1, 1, 2, 0)
        tr.move(1, 1)
        self.assertEqual(str(tr), "[(1, 1), (2, 2), (3, 1)]")


if __name__ == '__main__':
    unittest.main()
