#!/usr/bin/python3
""" 8-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

        r1 = Rectangle(10, 10, 10, 10)
        print(r1)

        r1.update(height=100)
        print(r1)

        r1.update(x = 10000, y = 99999, id = 458)
        print(r1)
