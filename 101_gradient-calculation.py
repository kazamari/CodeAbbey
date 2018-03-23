'''
You are given a function in the form (with A, B and C being some constants):

f = f(x, y) = (x - A)^2 + (y - B)^2 + C * exp(- (x + A)^2 - (y + B)^2)

It looks like a wide bowl having small peak somewhere inside, see the pictures above.

You will be given some points, as pairs of coordinates (x, y) and asked about the direction of the descent from this point.

Input data will contain four values in the first line: N - the number of points, then constants A, B and C.
Next lines will contain one point each, as a pair of cooridnates X and Y.
Answer should give integers in range from 0 to 360 - the direction of the descent of the slope in each of the points, expressed in degrees and rounded to whole integers.

Example:

input data:
14 -0.5 -0.4 7
0.3 0.2
0.4 -0.5
-0.7 0.1
-0.7 -0.7
0.3 0
0.6 -0.5
-1 -0.7
-0.8 0.8
-0.2 0.9
0.1 -0.4
0.4 -0.6
0.6 -0.5
-0.2 0.8
-0.8 0.2

answer:
222 246 211 212 234 254 19 214 172 234 244 254 175 213
'''
import math
from sys import stdin


def get_dir(A, B, C, coords):
    dt, res = 1e-9, []
    f = lambda x, y: (x - A)**2 + (y - B)**2 + C * math.e**(-(x + A)**2 - (y + B)**2)
    for x, y in coords:
        fxy = f(x, y)
        fdxy = f(x + dt, y)
        fxdy = f(x, y + dt)
        gx, gy = (fdxy - fxy) / dt, (fxdy - fxy) / dt
        res.append(round(math.degrees(math.atan2(gy, gx))) + 180)
    return res


given = [line.rstrip() for line in stdin]
n, A, B, C = map(float, given[0].split())
coords = [[float(x) for x in c.split()] for c in given[1:]]

print(*get_dir(A, B, C, coords))

