'''
Input data contain the number of stars N and the rotation angle A (counterclockwise, from 0 to 360 degrees).
Next lines will contain data about one star each in form Name X Y. Coordnates would be integer, not exceeding 1000 in
absolute value.
Answer should give the names of stars sorted by Y and then by X after rotation (and rounding).

Note: sorting should be performed in ascending order, i.e. from smallest values to largest.

Example:

input data:
4 45
Deneb -10 10
Algol 10 10
Sirius -10 -10
Mira 10 -10

answer:
Sirius Deneb Mira Algol
'''
from sys import stdin
import math


def ccw(x, y, c):
    alpha = math.atan2(y, x) + math.radians(c)
    R = math.sqrt(x ** 2 + y ** 2)
    return [round(R * math.cos(alpha)), round(R * math.sin(alpha))]


c, dict = 0, {}
for i, line in enumerate(stdin):
    if i == 0:
        c = int(line.rstrip().split()[1])
    else:
        name, coords = line.rstrip().split(' ', 1)
        dict.update({name: list(map(int, coords.split()))})

dict_ccw = {key: ccw(*value, c) for key, value in dict.items()}

print(*[x[0] for x in sorted(dict_ccw.items(), key=lambda x: (x[1][1], x[1][0]))])