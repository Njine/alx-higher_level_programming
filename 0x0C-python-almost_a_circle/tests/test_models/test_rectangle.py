import unittest
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleMethods(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_new_rectangle(self):
        new = Rectangle(1, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_new_rectangle_with_attrs(self):
        new = Rectangle(2, 3, 5, 5, 4)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)

    def test_new_rectangles(self):
        new = Rectangle(1, 1)
        new2 = Rectangle(1, 1)
        self.assertNotEqual(new, new2)
        self.assertNotEqual(new.id, new2.id)

    def test_base_instance(self):
        new = Rectangle(1, 1)
        self.assertTrue(isinstance(new, Base))

    def test_incorrect_amount_of_attributes(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_access_private_attributes(self):
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__width

    def test_validate_attributes(self):
        with self.assertRaises(TypeError):
            Rectangle("2", 2, 2, 2, 2)

    def test_validate_attributes_values(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 1)

    def test_area_method(self):
        new = Rectangle(4, 5)
        self.assertEqual(new.area(), 20)
        new.width = 5
        self.assertEqual(new.area(), 25)

    def test_display_method(self):
        r1 = Rectangle(2, 5)
        expected_output = "##\n##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), expected_output)

    def test_to_string_method(self):
        r1 = Rectangle(2, 5, 2, 4)
        expected_output = "[Rectangle] (1) 2/4 - 2/5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), expected_output)

    def test_to_dictionary_method(self):
        r1 = Rectangle(1, 2, 3, 4, 1)
        expected_output = "[Rectangle] (1) 3/4 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), expected_output)

        dictionary = r1.to_dictionary()
        self.assertEqual(type(dictionary), dict)

    def test_dict_to_json(self):
        r1 = Rectangle(2, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        expected_output = "[{}]\n".format(dictionary.__str__())
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), expected_output.replace("'", "\""))


if __name__ == '__main__':
    unittest.main()
