#!/usr/bin/python3
"""Defines a class Base."""
import json
import csv
import turtle


class Base:
    """Class Base."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of class base with one parameter id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list of dictionaries.
        Args:
            1. list_dictionary: List of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.
        Args:
            1. list_objs: List of inherited base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dictionary = [i.to_dictionary() for i in list_objs]
                file.write(Base.to_json_string(list_dictionary))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.
        Args:
            1. json_string: string representing a list of dictionaries.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.
        Args:
            1. dictionary: A dictionary.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                tmp = cls(1, 1)
            else:
                tmp = cls(1)
            tmp.update(**dictionary)
            return tmp

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        filen = str(cls.__name__) + ".json"
        try:
            with open(filen, "r") as file_n:
                list_dictionary = Base.from_json_string(file_n.read())
                return [cls.create(**d) for d in list_dictionary]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV serialization of a list of objects to a file.
        Args:
            1.list_objs (list): A list of inherited Base instances.
        """
        filen = cls.__name__ + ".csv"
        with open(filen, "w", newline="") as file_n:
            if list_objs is None or list_objs == []:
                file_n.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                d_writer = csv.DictWriter(file_n, fieldnames=fieldnames)
                for i in list_objs:
                    d_writer.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances."""
        filen = cls.__name__ + ".csv"
        try:
            with open(filen, "r", newline="") as file_n:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(file_n, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares.
        Args:
           1. list_rectangles: List of Rectangle objects to draw.
           2. list_squares: A list of Square objects to draw.
        """
        turt1 = turtle.Turtle()
        turt1.screen.bgcolor("#C2DFFF")
        turt1.pensize(3)
        turt1.shape("turtle")

        turt1.color("#000000")
        for rect in list_rectangles:
            turt1.showturtle()
            turt1.up()
            turt1.goto(rect.x, rect.y)
            turt1.down()
            for i in range(2):
                turt1.forward(rect.width)
                turt1.left(90)
                turt1.forward(rect.height)
                turt1.left(90)
            turt1.hideturtle()

        turt1.color("FF0000")
        for sqr in list_squares:
            turt1.showturtle()
            turt1.up()
            turt1.goto(sqr.x, sqr.y)
            turt1.down()
            for i in range(2):
                turt1.forward(sqr.width)
                turt1.left(90)
                turt1.forward(sqr.height)
                turt1.left(90)
            turt1.hideturtle()

        turtle.exitonclick()
