'''
Input data contains the number of triangles in the first line.
Next lines describe one triangle each. Descriptions consist of three values - lengths of sides. Largest value would
always be the last of three for simplicity.
Answers should have one of the letters R (right), A (acute) or O (obtuse) for each of triangles. Letters should be
separated by spaces.

Example:

input data:
3
6 8 9
9 12 15
16 12 22

answer:
A R O
'''

import sys


def check_triangle(a, b, c):
    a2b2 = (a**2 + b**2)**(1/2)
    if a2b2 > c:
        return 'A'
    elif a2b2 < c:
        return 'O'
    else:
        return 'R'


n = int(input())
print(*[check_triangle(*list(map(int, line.rstrip().split()))) for line in sys.stdin])
