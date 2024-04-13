import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 0, "test"), 1)
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([1, 2, 3], 2, "test"), 3)
        self.assertEqual(arrs.get([], 0, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 3], 10, "test"), "test")

    def test_slice(self):
        assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
        assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
        assert arrs.my_slice([], 1, 3) == []
        assert arrs.my_slice([1, 2, 3, 4]) == [1, 2, 3, 4]
        assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
        assert arrs.my_slice([1, 2, 3, 4], 1) == [2, 3, 4]
        assert arrs.my_slice([1, 2, 3, 4], end=3) == [1, 2, 3]
        assert arrs.my_slice([1, 2, 3, 4], -3, -1) == [2, 3]