import unittest
from io import StringIO
from unittest.mock import patch
from models.square import Square
from models.base import Base


class TestSquareMethods(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_new_square(self):
        new = Square(3)
        self.assertEqual(new.size, 3)
        self.assertEqual(new.width, 3)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_new_square_with_attrs(self):
        new = Square(2, 5, 5, 4)
        self.assertEqual(new.size, 2)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 2)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)

    def test_square_instances(self):
        new = Square(1, 1)
        new2 = Square(1, 1)
        self.assertNotEqual(new, new2)
        self.assertNotEqual(new.id, new2.id)

    def test_base_instance(self):
        new = Square(1)
        self.assertTrue(isinstance(new, Base))

    def test_rectangle_instance(self):
        new = Square(1)
        self.assertTrue(isinstance(new, Square))

    def test_invalid_amount_of_attributes(self):
        with self.assertRaises(TypeError):
            Square()

    def test_access_private_attributes(self):
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__width

    def test_validate_attributes(self):
        with self.assertRaises(TypeError):
            Square("2", 2, 2, 2)

    def test_validate_attributes_values(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_area_method(self):
        new = Square(4)
        self.assertEqual(new.area(), 16)
        new.size = 5
        self.assertEqual(new.area(), 25)

    def test_display_method(self):
        r1 = Square(2)
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), "##\n##")

    def test_to_string_method(self):
        r1 = Square(4, 2, 2)
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), "[Square] (1) 2/2 - 4\n")

    def test_update_method(self):
        s1 = Square(3)
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), "[Square] (1) 0/0 - 3\n")

        s1.update(5)
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), "[Square] (5) 0/0 - 3\n")

    def test_to_dictionary_method(self):
        s1 = Square(1, 2, 3)
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), "[Square] (1) 2/3 - 1\n")

        dictionary = s1.to_dictionary()
        self.assertEqual(type(dictionary), dict)

    def test_dict_to_json(self):
        s1 = Square(2)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, '[{"id": 1, "size": 2, "x": 0, "y": 0}]')


if __name__ == '__main__':
    unittest.main()
