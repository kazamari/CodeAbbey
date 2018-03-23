'''
Now we are to help the old forestry master to measure heights of several trees. For each tree you are told the distance
D to it and also the angle B between the line of sight (to the top) and the vertical line given by plumb. So the angle
B is 90 degrees when line of sight is horizontal and is 120 degrees when the line of sight is raised 30 degrees above
horizont - it is up to you to guess how A should be calculated from B :)

Input data will contain the amount of the trees we want to measure in the first line.
Next lines will contain a pair of values D and B each (one line for each tree), angle is specified in degrees.
Answer should contain the heights of the trees in the same order, rounded to nearest integer.

Example:

input data:
3
71 134.182
47 139.994
121 109.983

answer:
69 56 44
'''
from math import tan, radians
from sys import stdin


def tree_height(d, b):
    return round(d * tan(radians(b - 90)))


print(*[tree_height(d, b) for d, b in [map(float, line.rstrip().split()) for i, line in enumerate(stdin) if i > 0]])
