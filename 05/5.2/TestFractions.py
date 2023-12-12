import unittest
from fracs import add_frac, sub_frac, mul_frac, div_frac, is_positive, is_zero, cmp_frac, frac2float


class TestFractions(unittest.TestCase):
    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([1, 8], [1, 8]), [2, 8])
        self.assertEqual(add_frac([6, 100], [4, 100]), [10, 100])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 2]), [0, 2])
        self.assertEqual(sub_frac([1, 5], [1, 10]), [1, 10])
        self.assertEqual(sub_frac([6, 6], [10, 8]), [-6, 24])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 2]), [1, 4])
        self.assertEqual(mul_frac([1, 5], [-3, 4]), [-3, 20])
        self.assertEqual(mul_frac([0, 12], [10, 8]), [0, 96])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 2]), [2, 2])
        self.assertEqual(div_frac([1, 5], [-3, 4]), [4, -15])
        self.assertEqual(div_frac([0, 12], [10, 8]), [0, 120])

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertFalse(is_positive([-1, 5]))
        self.assertFalse(is_positive([0, 12]))

    def test_is_zero(self):
        self.assertFalse(is_zero([1, 2]))
        self.assertFalse(is_zero([-1, 5]))
        self.assertTrue(is_zero([0, 12]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 2]), 0)
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 3], [1, 2]), -1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)
        self.assertEqual(frac2float([3, 4]), 0.75)
        self.assertEqual(frac2float([2, 1]), 2.0)

    def tearDown(self):
        self.zero.clear()


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
