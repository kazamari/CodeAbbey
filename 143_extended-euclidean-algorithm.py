'''
Input data will contain the number of test cases on the first line.
Next lines will contain a pair of values each.
Answer should contain three values for each case - r a b separated with spaces - triplets themselves should be separated with spaces also.

Example:

input data:
3
23 7
31132 24144
22444 83452

1 -3 10
4 1807 -2330
124 264 -71
'''
from sys import stdin


def egcd(a, b):
    s1, s2, t1, t2 = 1, 0, 0, 1
    while b > 0:
        s1, s2 = s2, s1 - (a // b) * s2
        t1, t2 = t2, t1 - (a // b) * t2
        a, b = b, a % b
    return a, s1, t1


for a, b in [map(int, line.rstrip().split()) for i, line in enumerate(stdin) if i > 0]:
    print(*egcd(a, b))
