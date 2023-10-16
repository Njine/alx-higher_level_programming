import unittest
from models.base import Base
from io import StringIO
from models.square import Square
from models.rectangle import Rectangle 
from unittest.mock import patch
import os


class TestBaseMethods(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_default(self):
        new = Base()
        self.assertEqual(new.id, 1)

    def test_id_assigned(self):
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_id_incremented(self):
        new = Base()
        new2 = Base()
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 3)

    def test_id_mixed_assignment(self):
        new = Base()
        new2 = Base(1024)
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 1024)
        self.assertEqual(new3.id, 2)

    def test_string_id(self):
        new = Base('1')
        self.assertEqual(new.id, '1')

    def test_additional_args(self):
        with self.assertRaises(TypeError):
            new = Base(1, 1)

    def test_access_private_attrs(self):
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects

    def test_save_to_file_square(self):
        """Remove the file if it exists to ensure a clean test."""
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_rectangle(self):
        """Remove the file if it exists to ensure a clean test."""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")


if __name__ == '__main__':
    unittest.main()
