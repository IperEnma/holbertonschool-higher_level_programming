#!/usr/bin/python3
"""unittest for rectangle class"""

import io
from contextlib import redirect_stdout
import unittest
from models.rectangle import Rectangle


class test_rectangle(unittest.TestCase):
    """class test rectangle class"""

    instance = Rectangle(10, 10, 10, 10, 10)
    instance1 = Rectangle(10, 2)
    instance2 = Rectangle(2, 10)
    instance3 = Rectangle(10, 2, 0, 0, 12)
    instance4 = Rectangle(5, 5, 1)
    instance5 = Rectangle(4, 6, 2, 1, 12)
    instance6 = Rectangle(2, 3, 2, 2)

    def test_doc_class(self):
        """checking docstring"""
        self.assertGreater(len(self.instance1.__doc__), 1)

    def test_id_instance(self):
        """checking id assignment"""
        self.assertEqual(self.instance1.id, 1)
        self.assertEqual(self.instance2.id, 2)
        self.assertEqual(self.instance3.id, 12)

    def test_validation_string(self):
        """checking validation setter"""
        self.assertRaises(TypeError, Rectangle, 10, "2")
        self.assertRaises(ValueError, Rectangle, 10, 2, 3, -1)

        with self.assertRaises(Exception) as Error:
            self.instance1.width = {}
        self.assertEqual('width must be an integer', str(Error.exception))

        with self.assertRaises(Exception) as Error:
            self.instance1.width = -10
        self.assertEqual('width must be > 0', str(Error.exception))

    def test_area(self):
        """test calculate area"""
        self.assertEqual(self.instance1.area(), 20)
        self.instance2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(self.instance2.area(), 56)

    def test_display_0(self):
        """test display representation with characters '#'"""
        with redirect_stdout(io.StringIO()) as buff:
            self.instance1.display()
        self.assertEqual(buff.getvalue(), (("#" * 10) + "\n") * 2)

        self.instance2 = Rectangle(2, 2)

        with redirect_stdout(io.StringIO()) as buff:
            self.instance2.display()
        self.assertEqual(buff.getvalue(), (("#" * 2) +"\n") * 2)

    def test_str(self):
        """test overriding the __str__"""

        with redirect_stdout(io.StringIO()) as buff:
            print(self.instance4)
        self.assertEqual(buff.getvalue(), "[Rectangle] (3) 1/0 - 5/5\n")

        with redirect_stdout(io.StringIO()) as buff:
            print(self.instance5)
        self.assertEqual(buff.getvalue(), "[Rectangle] (12) 2/1 - 4/6\n")

    def test_display_1(self):
        """test display representation with characters '#' plus position"""
        with redirect_stdout(io.StringIO()) as buff:
            self.instance4.display()
        self.assertEqual(buff.getvalue(), (" " + ("#" * 5) +"\n") * 5)

        with redirect_stdout(io.StringIO()) as buff:
            self.instance6.display()
        self.assertEqual(buff.getvalue(), "\n\n" + ("  " + ("#" * 2) +"\n") * 3)

    def test_update_0(self):
        """test method update"""
        self.instance.update(89)
        with redirect_stdout(io.StringIO()) as buff:
            print(self.instance)
        self.assertEqual(buff.getvalue(), "[Rectangle] (89) 10/10 - 10/10\n")

        self.instance.update(89, 2)
        with redirect_stdout(io.StringIO()) as buff:
            print(self.instance)
        self.assertEqual(buff.getvalue(), "[Rectangle] (89) 10/10 - 2/10\n")

        self.instance.update(89, 2, 3)
        with redirect_stdout(io.StringIO()) as buff:
            print(self.instance)
        self.assertEqual(buff.getvalue(), "[Rectangle] (89) 10/10 - 2/3\n")

        self.instance.update(89, 2, 3, 4)
        with redirect_stdout(io.StringIO()) as buff:
            print(self.instance)
        self.assertEqual(buff.getvalue(), "[Rectangle] (89) 4/10 - 2/3\n")

        self.instance.update(89, 2, 3, 4, 5)
        with redirect_stdout(io.StringIO()) as buff:
            print(self.instance)
        self.assertEqual(buff.getvalue(), "[Rectangle] (89) 4/5 - 2/3\n")

    def test_update_1(self):
        """test method update 1"""
        self.instance.update(10, 10, 10, 10, 10)

        self.instance.update(height=1)
        with redirect_stdout(io.StringIO()) as buff:
            print(self.instance)
        self.assertEqual(buff.getvalue(), "[Rectangle] (10) 10/10 - 10/1\n")

        self.instance.update(width=1, x=2)
        with redirect_stdout(io.StringIO()) as buff:
            print(self.instance)
        self.assertEqual(buff.getvalue(), "[Rectangle] (10) 2/10 - 1/1\n")

        self.instance.update(y=1, width=2, x=3, id=89)
        with redirect_stdout(io.StringIO()) as buff:
            print(self.instance)
        self.assertEqual(buff.getvalue(), "[Rectangle] (89) 3/1 - 2/1\n")

        self.instance.update(x=1, height=2, y=3, width=4)
        with redirect_stdout(io.StringIO()) as buff:
            print(self.instance)
        self.assertEqual(buff.getvalue(), "[Rectangle] (89) 1/3 - 4/2\n")

    def test_to_dictionary(self):
        """test metho to_dictionary"""
        self.assertEqual(self.instance6.to_dictionary(), {'id': 4, 'width': 2, 'height': 3, 'x': 2, 'y': 2})
        self.assertEqual(type(self.instance6.to_dictionary()), dict)
        self.assertEqual(self.instance5.to_dictionary(), {'id': 12, 'width': 4, 'height': 6, 'x': 2, 'y': 1})
        self.assertEqual(type(self.instance5.to_dictionary()), dict)
