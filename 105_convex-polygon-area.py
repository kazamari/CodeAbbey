'''
Polygon is called convex if each of its angles is less than PI/2, or in other words, if any line connecting any pair
of points belonging to it lies completely inside. This somewhat simplifies handling of such shapes.

You need to reduce this problem to one with triangles. We hope that pictures above may give you idea on three different
approaches to do this.

Input data contain the number of vertices of the polygon.
Next lines contain a pair of numbers each - X and Y coordinates for the vertex (in correct CCW order).
Answer should contain the area of the shape surrounded by these points.

Example:

input data:
5
51 9
77 10
92 71
62 84
29 94

answer:
3274.5
'''
from sys import stdin


def s_tr(x1, y1, x2, y2, x3, y3):
    return 0.5 * abs((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3))


def s_poly(polygon):
    x1, y1 = polygon[0]
    return sum([s_tr(x1, y1, polygon[i][0], polygon[i][1], polygon[i+1][0], polygon[i+1][1]) for i in range(1, len(polygon)-1)])


polygon = [list(map(int, line.rstrip().split())) for i, line in enumerate(stdin) if i > 0]
print(s_poly(polygon))