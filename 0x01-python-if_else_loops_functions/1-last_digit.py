#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
if number < 0:
    last_digit = -1 * last_digit

sout = 'Last digit of ' + str(number) + ' is ' + str(last_digit)

sdisplay = ''

if last_digit > 5:
    sdisplay = ' and is greater than 5'
elif last_digit == 0:
    sdisplay = ' and is 0'
else:
    sdisplay = ' and is less than 6 and not 0'

print(f"{sout}{sdisplay}")
