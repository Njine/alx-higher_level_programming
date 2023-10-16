#!/usr/bin/python3
"""Module contains class Base."""
import json
import os.path
import csv


class Base:
    """Class Base."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize instance with an optional ID."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string."""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save objects to a JSON file."""
        filename = f"{cls.__name__}.json"
        list_dic = [obj.to_dictionary() for obj in list_objs] if list_objs else []

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dic))

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries."""
        return json.loads(json_string) if json_string else []

    @classmethod
    def create(cls, **dictionary):
        """Create an instance and update it with the provided dictionary."""
        new = cls(10, 10) if cls.__name__ == "Rectangle" else cls(10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from a JSON file."""
        filename = f"{cls.__name__}.json"

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_ins = [cls.create(**dict_obj) for dict_obj in list_cls]

        return list_ins

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save objects to a CSV file."""
        filename = f"{cls.__name__}.csv"
        
        list_keys = ['id', 'width', 'height', 'x', 'y'] if cls.__name__ == "Rectangle" else ['id', 'size', 'x', 'y']
        matrix = []

        if list_objs:
            matrix = [[obj.to_dictionary()[key] for key in list_keys] for obj in list_objs]

        with open(filename, 'w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """Load objects from a CSV file and return a list of instances."""
        filename = f"{cls.__name__}.csv"

        if not os.path.exists(filename):
            return []

        with open(filename, 'r', newline='') as readFile:
            reader = csv.reader(readFile)
            csv_list = list(reader)

        list_keys = ['id', 'width', 'height', 'x', 'y'] if cls.__name__ == "Rectangle" else ['id', 'size', 'x', 'y']
        matrix = []

        for csv_elem in csv_list:
            dict_csv = {key: int(value) for key, value in zip(list_keys, csv_elem)}
            matrix.append(dict_csv)

        list_ins = [cls.create(**dict_obj) for dict_obj in matrix]

        return list_ins
