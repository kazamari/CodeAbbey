'''
Being able to calculate area of triangle is quite important since many more complex tasks are often easily reduced to
this (and we will use it too later).

One of the oldest known methods is Heron's Formula which takes as inputs the lengths of the triangle's sides.

In this problem you however is to write a program which uses X and Y coordinates of the triangle's vertices instead.
So you can use either this formula somehow or find another one.

Input data will contain the number of triangles to process.
Next lines will contain 6 values each, in order X1 Y1 X2 Y2 X3 Y3, describing three vertices of a triangle.
Answer should give areas of triangles separated by space (precision about 1e-7 is expected).

Example:

data:
3
1 3 9 5 6 0
1 0 0 1 10000 10000
7886 5954 9953 2425 6250 2108

answer:
17 9999.5 6861563
'''
# from math import sqrt
import sys


def s_tr(x1, y1, x2, y2, x3, y3):
    return 0.5 * abs((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3))

# def heron(x1, y1, x2, y2, x3, y3):
#     a = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
#     b = ((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3)) ** 0.5
#     c = ((x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1)) ** 0.5
#     p = (a + b + c) / 2
#     return (p * (p - a) * (p - b) * (p - c)) ** 0.5
#
# def triangleArea(x1, y1, x2, y2, x3, y3):
#     a = sqrt((x2 - x1)**2 + (y2-y1)**2) # Distance between A and B
#     b = sqrt((x3 - x1)**2 + (y3-y1)**2) # Distance between A and C
#     c = sqrt((x3 - x2)**2 + (y3-y2)**2) # Distance between B and C
#     s = (a + b + c) / 2 # s  = Semiperimeter
#     return sqrt(s*((s-a)*(s-b)*(s-c))) # Heron's Formula


print(*[s_tr(*map(int, line.rstrip().split())) for i, line in enumerate(sys.stdin) if i > 0])

