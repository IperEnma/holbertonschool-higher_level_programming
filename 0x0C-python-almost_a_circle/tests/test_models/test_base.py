#!/usr/bin/python3
"""unittests for the function
"""

import io
from contextlib import redirect_stdout
import unittest
from models.base import Base
from models.rectangle import Rectangle


class test_base(unittest.TestCase):
    """class test base class"""

    def test_base(self):
        """test base checking"""
        base0 = Base(1)
        self.assertEqual(base0.id, 1)
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)

    def test_doc_class(self):
        """checking docstring"""
        self.assertGreater(len(Base().__doc__), 1)

    def test_create(self):
        """checking create class"""
        testclass = Base()
        self.assertTrue(testclass.id, 1)

    def test_id(self):
        """checking id"""
        testclass = Base(12)
        self.assertEqual(testclass.id, 12)

    def test_moreid(self):
        """checking more id"""
        with self.assertRaises(Exception) as Err:
            testclass = Base(12, 12)

    def test_to_jsonstring(self):
        """checking method to_json_string"""
        self.r1 = Rectangle(10, 7, 2, 8)
        self.dictionary = self.r1.to_dictionary()
        self.json_dictionary = Base.to_json_string([self.dictionary])

        with redirect_stdout(io.StringIO()) as buff:
            print(self.json_dictionary)
        self.assertEqual(buff.getvalue(), '[{"id": 12, "width": 10,\
 "height": 7, "x": 2, "y": 8}]\n')
        self.assertEqual(type(buff.getvalue()), str)

    def test_save_to_file(self):
        """checking method save file"""
        self.r1 = Rectangle(10, 7, 2, 8)
        self.r2 = Rectangle(2, 4)
        Rectangle.save_to_file([self.r1, self.r2])

        with open("Rectangle.json") as f:
            self.read = f.read()
        self.assertEqual(self.read, '[{"id": 10, "width": 10, "height": 7, "x":\
 2, "y": 8}, {"id": 11, "width": 2, "height": 4, "x": 0, "y": 0}]')

    def test_from_json_string(self):
        """checking from json string"""
        self.list_input = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
                ]
        self.json_list_input = Rectangle.to_json_string(self.list_input)
        self.list_output = Rectangle.from_json_string(self.json_list_input)

        self.assertEqual(type(self.list_input), list)
        self.assertEqual(type(self.json_list_input), str)
        self.assertEqual(type(self.list_output), list)

        with redirect_stdout(io.StringIO()) as _str:
            print(self.list_input)
        self.assertEqual(_str.getvalue(), "[{'id': 89, 'width': 10, 'height':\
 4}, {'id': 7, 'width': 1, 'height': 7}]\n")

        with redirect_stdout(io.StringIO()) as _str:
            print(self.json_list_input)
        self.assertEqual(_str.getvalue(), '[{"id": 89, "width": 10, "height":\
 4}, {"id": 7, "width": 1, "height": 7}]\n')

        with redirect_stdout(io.StringIO()) as _str:
            print(self.list_output)
        self.assertEqual(_str.getvalue(), "[{'id': 89, 'width': 10, 'height':\
 4}, {'id': 7, 'width': 1, 'height': 7}]\n")

    def test_create(self):
        """test create checking"""
        self.r3 = Rectangle(3, 5, 1)
        self.r3_dictionary = self.r3.to_dictionary()
        self.r4 = Rectangle.create(**self.r3_dictionary)

        with redirect_stdout(io.StringIO()) as _str:
            print(self.r3)
        self.assertEqual(_str.getvalue(), "[Rectangle] (3) 1/0 - 3/5\n")

        with redirect_stdout(io.StringIO()) as _str:
            print(self.r4)
        self.assertEqual(_str.getvalue(), "[Rectangle] (3) 1/0 - 3/5\n")
        compare = self.r3 is self.r4
        self.assertEqual(compare, False)
        compare = self.r3 == self.r4
        self.assertEqual(compare, False)

    def test_load_from_file(self):
        """test create instance from file"""
        self.r1 = Rectangle(10, 7, 2, 8)
        self.r2 = Rectangle(2, 4)
        self.list_rectangles_input = [self.r1, self.r2]

        Rectangle.save_to_file(self.list_rectangles_input)

        self.list_rectangles_output = Rectangle.load_from_file()

        with redirect_stdout(io.StringIO()) as str_copy:
            print(self.list_rectangles_output[0])
        self.assertEqual(str_copy.getvalue(), "[Rectangle] (6) 2/8 - 10/7\n")

        with redirect_stdout(io.StringIO()) as str_origin:
            print(self.list_rectangles_input[0])
        self.assertEqual(str_origin.getvalue(), "[Rectangle] (6) 2/8 - 10/7\n")
        self.assertEqual(str_origin.getvalue(), str_copy.getvalue())

        with redirect_stdout(io.StringIO()) as str_copy:
            print(self.list_rectangles_output[1])
        self.assertEqual(str_copy.getvalue(), "[Rectangle] (7) 0/0 - 2/4\n")

        with redirect_stdout(io.StringIO()) as str_origin:
            print(self.list_rectangles_input[1])
        self.assertEqual(str_origin.getvalue(), "[Rectangle] (7) 0/0 - 2/4\n")
        self.assertEqual(str_origin.getvalue(), str_copy.getvalue())

if __name__ == '__main__':
    unittest.main()
