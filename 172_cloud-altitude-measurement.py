'''
Input data will contain the amount of clouds (or aircrafts) we are curious about.
Each line describes D1, A and B for a single cloud.
Answer should contain altitudes of the objects, rounded to nearest integer.

Example:

input data:
3
1859 23.7740 53.8740
1721 34.2290 68.1863
1512 26.0048 53.1380

answer:
1207 1609 1163
'''
import math
from sys import stdin


def cloud_alt(d1, a, b):
    ta, tb = math.tan(math.radians(a)), math.tan(math.radians(b))
    return round((ta * tb * d1) / (tb - ta))


print(*[cloud_alt(*map(float, line.rstrip().split())) for i, line in enumerate(stdin) if i > 0])