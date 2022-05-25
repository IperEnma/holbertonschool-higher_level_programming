#!/usr/bin/python3
"""unittests for the function
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """class tester for max_integer"""

    def test_docfunction(self):
        """checking documentation"""
        self.assertTrue(len(max_integer.__doc__), 1)

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
        self.assertRaises(TypeError, max_integer, [None, 3, 5])
        self.assertRaises(TypeError, max_integer, [None, None, None])

    def test_strings(self):
        """checking strings"""
        self.assertRaises(TypeError, max_integer, [1, 3, 5, "Hola"])

    def test_boolean(self):
        """ test boolean"""
        self.assertRaises(TypeError, max_integer, [2, 4, 6j])

    def test_dictionary(self):
        self.assertRaises(TypeError, max_integer, {2, 4, 6})

    def test_tupla(self):
        self.assertEqual(max_integer((1, 2, 3)), 3)

    def test_listoflist(self):
        self.assertRaises(TypeError, max_integer, [1, [2, 4], 3])

    def test_stringssss(self):
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_int_char(self):
        self.assertRaises(TypeError, max_integer, [2j, 3, 5])

    def test_empty(self):
        self.assertRaises(TypeError, max_integer, None)


if __name__ == '__main__':
    """function main"""
    unittest.main()
