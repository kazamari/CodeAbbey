'''
Input data contain number of test-cases in the first line.
Each of the following lines contain three numbers S, R and P.
Answer should contain number of years to wait for each case, separated by spaces.

Example:

input data:
2
1000 10000 8
50 100 25

answer:
30 4
'''

import sys


def floor(x):
    return x if (x * 1000) % 10 == 0 else round((x - 0.005), 2)


def years(s, r, p):
    y = 0
    while s < r:
        s = floor(s * (1 + p / 100))
        y += 1
    return y


n = int(input())
for line in sys.stdin:
    s, r, p = map(int, line.rstrip().split())
    print(years(s, r, p), end=" ")
