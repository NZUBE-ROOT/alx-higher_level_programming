#!/usr/bin/python3
for k in range(0, 100):
    if k == 99:
        print('{0}'.format(k))
    else:
        print('{:02}'.format(k), end=', ')
