#!/usr/bin/python3
"""unittest for square class"""

import io
from contextlib import redirect_stdout
import unittest
from models.square import Square


class SquareTest(unittest.TestCase):
    """class test Square class"""

    instance1 = Square(5)
    instance2 = Square(2, 2)
    instance3 = Square(3, 1, 3)

    def test_basic(self):
        """test cases basic square"""
        with redirect_stdout(io.StringIO()) as _str:
            print(self.instance1)
        with redirect_stdout(io.StringIO()) as buff:
            self.instance1.display()
        self.assertEqual(buff.getvalue(), (("#" * 5) + "\n") * 5)
        self.assertEqual(_str.getvalue(), "[Square] (5) 0/0 - 5\n")
        self.assertEqual(self.instance1.area(), 25)

        with redirect_stdout(io.StringIO()) as _str:
            print(self.instance2)
        with redirect_stdout(io.StringIO()) as buff:
            self.instance2.display()
        self.assertEqual(buff.getvalue(), ("  " + ("#" * 2) + "\n") * 2)
        self.assertEqual(_str.getvalue(), "[Square] (6) 2/0 - 2\n")
        self.assertEqual(self.instance2.area(), 4)

        with redirect_stdout(io.StringIO()) as _str:
            print(self.instance3)
        with redirect_stdout(io.StringIO()) as b:
            self.instance3.display()
        self.assertEqual(b.getvalue(), "\n\n\n" + (" " + ("#" * 3) + "\n") * 3)
        self.assertEqual(_str.getvalue(), "[Square] (7) 1/3 - 3\n")
        self.assertEqual(self.instance3.area(), 9)

    def test_size(self):
        """test setter ang getter size"""
        self.instance1.update(1, 5, 0, 0)
        with redirect_stdout(io.StringIO()) as _str:
            print(self.instance1)
        self.assertEqual(_str.getvalue(), "[Square] (1) 0/0 - 5\n")
        self.assertEqual(self.instance1.size, 5)

        self.instance1.size = 10
        with redirect_stdout(io.StringIO()) as _str:
            print(self.instance1)
        self.assertEqual(_str.getvalue(), "[Square] (1) 0/0 - 10\n")
        self.assertEqual(self.instance1.size, 10)

        with self.assertRaises(Exception) as Error:
            self.instance1.size = "9"
        self.assertEqual("width must be an integer", str(Error.exception))

    def test_update(self):
        """test update square"""
        self.instance1.update(1, 5, 0, 0)
        with redirect_stdout(io.StringIO()) as _str:
            print(self.instance1)
        self.assertEqual(_str.getvalue(), "[Square] (1) 0/0 - 5\n")

        self.instance1.update(10)
        with redirect_stdout(io.StringIO()) as _str:
            print(self.instance1)
        self.assertEqual(_str.getvalue(), "[Square] (10) 0/0 - 5\n")

        self.instance1.update(1, 2)
        with redirect_stdout(io.StringIO()) as _str:
            print(self.instance1)
        self.assertEqual(_str.getvalue(), "[Square] (1) 0/0 - 2\n")

        self.instance1.update(1, 2, 3)
        with redirect_stdout(io.StringIO()) as _str:
            print(self.instance1)
        self.assertEqual(_str.getvalue(), "[Square] (1) 3/0 - 2\n")

        self.instance1.update(1, 2, 3, 4)
        with redirect_stdout(io.StringIO()) as _str:
            print(self.instance1)
        self.assertEqual(_str.getvalue(), "[Square] (1) 3/4 - 2\n")

        self.instance1.update(x=12)
        with redirect_stdout(io.StringIO()) as _str:
            print(self.instance1)
        self.assertEqual(_str.getvalue(), "[Square] (1) 12/4 - 2\n")

        self.instance1.update(size=7, y=1)
        with redirect_stdout(io.StringIO()) as _str:
            print(self.instance1)
        self.assertEqual(_str.getvalue(), "[Square] (1) 12/1 - 7\n")

        self.instance1.update(size=7, id=89, y=1)
        with redirect_stdout(io.StringIO()) as _str:
            print(self.instance1)
        self.assertEqual(_str.getvalue(), "[Square] (89) 12/1 - 7\n")

    def test_to(self):
        """test to_dictionary square"""
        self.assertEqual(
                self.instance2.to_dictionary(),
                {
                    'id': 6,
                    'size': 2,
                    'x': 2,
                    'y': 0
                })
        self.assertEqual(type(self.instance2.to_dictionary()), dict)
        self.assertEqual(
                self.instance3.to_dictionary(),
                {
                    'id': 7,
                    'size': 3,
                    'x': 1,
                    'y': 3
                })
        self.assertEqual(type(self.instance3.to_dictionary()), dict)

if __name__ == '__main__':
    unittest.main()
