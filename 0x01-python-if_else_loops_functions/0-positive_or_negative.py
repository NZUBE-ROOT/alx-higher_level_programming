#!/usr/bin/python3
import random
number = random.randint(-10, 10)
sout = ''

if number > 0:
    sout = 'is positive'
elif number == 0:
    sout = 'is zero'
else:
    sout = 'is negative'

print(f"{number} {sout}")
