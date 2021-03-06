#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""

    def test_max_integer(self):
        """ tests"""
        self.assertEqual(max_integer(""), None)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer("azerty"), "z")
        self.assertEqual(max_integer([3, 5, 8]), 8)
        self.assertEqual(max_integer([14, -1, 13]), 14)
        self.assertEqual(max_integer([0, 7, 7, -3]), 7)
        self.assertEqual(max_integer([5, 5, 9, 8, 9, 5]), 9)
        self.assertEqual(max_integer([[9, 0], [2, 18]]), [9, 0])
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-1, -82, -43, -45]), -1)
        str1 = ["a", "b", "c"]
        self.assertEqual(max_integer(str1), "c")
        str = [1, 8, "Hello", 7, 5]
        with self.assertRaises(TypeError):
            max_integer(str)
    if __name__ == "__main__":
        unittest.main()
