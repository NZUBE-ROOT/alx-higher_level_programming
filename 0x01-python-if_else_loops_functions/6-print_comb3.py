#!/usr/bin/python3
for k in range(0, 10):
    for j in range(k + 1, 10):
        if k == 8 and j == 9:
            print('{0}{1}'.format(k, j))
        else:
            print('{0}{1}'.format(k, j), end=', ')
