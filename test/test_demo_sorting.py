import unittest
import demo_sorting

class TestDemoSorting(unittest.TestCase):
    def test_qdsort(self):
        data = [1, 2, 3]
        self.assertEqual(sorted(data), demo_sorting.qdsort(data))