import unittest
import demo_sorting

class TestDemoSorting(unittest.TestCase):
    def test_qdsort(self):
        data = [[1, 2, 3], [1, 3, 2], [2, 1]]
        for datum in data:
            with self.subTest(datum = datum):
                self.assertEqual(
                    sorted(datum), demo_sorting.qdsort(datum))