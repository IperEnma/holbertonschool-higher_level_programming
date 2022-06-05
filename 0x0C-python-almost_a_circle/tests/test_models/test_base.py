#!/usr/bin/python3
"""unittests for the function
"""

import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """class test base class"""

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
