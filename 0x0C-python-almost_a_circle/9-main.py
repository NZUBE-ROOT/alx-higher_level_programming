#!/usr/bin/python3
""" 9-main """
from models.square import Square

if __name__ == "__main__":

        s1 = Square(5)
        print(s1)
        print(s1.area())
        s1.display()

        print("------------")

        s2 = Square(2, 2)
        print(s2)
        print(s2.area())
        s2.display()
