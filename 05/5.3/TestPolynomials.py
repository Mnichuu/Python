import unittest
from polys import add_poly, sub_poly, mul_poly, is_zero, eq_poly, eval_poly, combine_poly, pow_poly, diff_poly


class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [0, 1]
        self.p2 = [0, 0, 1]

    def test_add_poly(self):
        self.assertEqual(add_poly([0, 1], [0, 0, 1]), [0, 1, 1])
        self.assertEqual(add_poly([1, 2, 3], [4, 5]), [1, 6, 8])

    def test_sub_poly(self):
        self.assertEqual(sub_poly([0, 1, 1], [0, 0, 1]), [0, 1, 0])
        self.assertEqual(sub_poly([1, 2, 3], [4, 5]), [-3, -3, 3])

    def test_mul_poly(self):
        self.assertEqual(mul_poly([1, 2], [1, 3]), [1, 5, 6])
        self.assertEqual(mul_poly([1, 2, 3], [4, 5]), [4, 13, 22, 15])

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 0, 0]))
        self.assertFalse(is_zero([1, 0, 0]))

    def test_eq_poly(self):
        self.assertTrue(eq_poly([1, 2, 3], [1, 2, 3]))
        self.assertFalse(eq_poly([1, 2, 3], [4, 5, 6]))

    def test_eval_poly(self):
        self.assertEqual(eval_poly([1, 2, 3], 2), 17)
        self.assertEqual(eval_poly([1, 0, 0, 1], 3), 28)

    def test_combine_poly(self):
        self.assertEqual(combine_poly([1, 2, 3], [2, 3, 4]), [17, 31, 53])
        self.assertEqual(combine_poly([1, 2, 3], [0, 1]), [6, 11])

    def test_pow_poly(self):
        self.assertEqual(pow_poly([1, 2], 3), [1, 6, 12, 8])
        self.assertEqual(pow_poly([1, 2, 3], 2), [1, 4, 10, 12, 9])

    def test_diff_poly(self):
        self.assertEqual(diff_poly([1, 2, 3]), [2, 6])
        self.assertEqual(diff_poly([1, 0, 0, 1]), [0, 0, 3])

    def tearDown(self):
        self.p1.clear()
        self.p2.clear()


if __name__ == '__main__':
    unittest.main()
