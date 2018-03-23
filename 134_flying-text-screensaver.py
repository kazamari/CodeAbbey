'''
Input data will contain Width and Height of the imaginary screen and the Length of text string.
Answer should dump pairs of coordinates X and Y of the beginning of the text for first 100 steps (spaces should be used
to separate values in the pair and pairs themselves) - i.e. 202 integers in total (including coordinates of the
starting position).

Coordinate system of the screen usually has the (0, 0) in the left top corner.

Example:

input data:
9 3 4

answer:
0 0 1 1 2 2 3 1 4 0 5 1 4 2 3 1 2 0 ... 4 0 3 1 2 2 1 1 0 0
'''


def steps(n):
    x, y, dx, dy = 0, 0, 1, 1
    coords = [(x, y)]
    for i in range(n):
        if x + dx < 0 or x + l == w:
            dx = -dx
        if y + dy < 0 or y + 1 == h:
            dy = -dy
        x += dx
        y += dy
        coords.append((x, y))
    return coords


w, h, l = map(int, input().split())
print(*[' '.join(map(str, pair)) for pair in steps(100)])
