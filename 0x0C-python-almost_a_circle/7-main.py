#!/usr/bin/python3
""" Doc """
from models.rectangle import Rectangle

if __name__ == "__main__":

        r1 = Rectangle(10, 10, 10, 10)
        print(r1)

        r1.update(89)
        print(r1)

        r1.update(100, 200, 300, 400)
        print(r1)
