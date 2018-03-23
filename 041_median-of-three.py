'''
Input data will contain in the first line the number of triplets to follow.
Next lines will contain one triplet each.
Answer should contain selected medians of triplets, separated by spaces.

Example:

data:
3
7 3 5
15 20 40
300 550 137

answer:
5 20 300

Note: if your program will have a lot of if-else-if-else statements, then you are probably doing something wrong.
Simple solution should have no more than three of them.
'''

import sys

def mediana(a, b, c):
    if a < b < c or c < b < a:
        return b
    elif a < c < b or b < c < a:
        return c
    else:
        return a

n = int(input())

print(*[mediana(*list(map(int, line.rstrip().split()))) for line in sys.stdin])
