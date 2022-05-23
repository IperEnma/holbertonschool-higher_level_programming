#!/usr/bin/python3
"""unittests for the function
"""

import unittest
max_integer = __import__('6-max_integer').max_integer
module = __import__('6-max_integer')

class TestMaxInt(unittest.TestCase):
    """class tester for max_integer"""
    
    def test_docmodule(self):
        """checking documentation"""
        self.assertTrue(len(module.__doc__), 1)

    def test_docfunction(self):
        """checking documentation"""
        self.assertTrue(len(module.__doc__), 1)

    def test_basic(self):
        """tests max integer basic"""
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_float(self):
        """tests max float"""
        self.assertEqual(max_integer([1.5, 2.7, 2.9]), 2.9)

    def test_negative(self):
        """test negative max integer"""
        self.assertEqual(max_integer([-1, 2, 100]), 100)

    def test_negative_all(self):
        """test max negative"""
        self.assertEqual(max_integer([-3, -5, -100]), -3)

    def test_none(self):
        """checking none args"""
        self.assertRaises(TypeError, lambda: max_integer([None, 3, 5]))

if __name__ == '__main__':
    unittest.main()
