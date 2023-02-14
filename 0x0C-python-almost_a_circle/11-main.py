#!/usr/bin/python3
""" 11-main """
from models.square import Square

if __name__ == "__main__":

        s1 = Square(5)
        print(s1)

        s1.update(10)
        print(s1)
        s1.update(11, 12, 13, 14)
        print(s1)

        s1.update(size=7, id=89, y=1)
        print(s1)

        s1.update(size=7, y=1)
        print(s1)
