'''
Input data contain the number of test-cases in the first line.
Next lines describe placement of the King and Queen for each testcase, by specifying their squares (King's first).
Answer should give only letter Y or N for each of test-cases, meaning that King could be taken or not respectively. Separate letters with spaces.

Example:

input data:
8
b4 b8
b4 e7
b4 d2
b4 g4
f2 b1
f2 c4
f2 d5
f2 g7

answer:
Y Y Y Y N N N N
'''

from sys import stdin

col = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}


def is_take(k, q):
    kx, ky = col[k[0]], int(k[1])
    qx, qy = col[q[0]], int(q[1])
    return 'Y' if kx == qx or ky == qy or abs(kx - qx) == abs(ky - qy) else 'N'


print(*[is_take(*line.rstrip().split()) for i, line in enumerate(stdin) if i > 0])
