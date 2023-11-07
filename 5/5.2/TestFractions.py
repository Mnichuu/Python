import unittest
import fracs


class TestFractions(unittest.TestCase):
    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(fracs.add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(fracs.add_frac([1, 8], [1, 8]), [2, 8])
        self.assertEqual(fracs.add_frac([6, 100], [4, 100]), [10, 100])

    def test_sub_frac(self):
        self.assertEqual(fracs.sub_frac([1, 2], [1, 2]), [0, 2])
        self.assertEqual(fracs.sub_frac([1, 5], [1, 10]), [1, 10])
        self.assertEqual(fracs.sub_frac([6, 6], [10, 8]), [-6, 24])
    def test_mul_frac(self): pass

    def test_div_frac(self): pass

    def test_is_positive(self): pass

    def test_is_zero(self): pass

    def test_cmp_frac(self): pass

    def test_frac2float(self): pass

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
