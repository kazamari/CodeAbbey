'''
Input data contain number of test-cases in the first line.
Then lines with test-cases follow, each containing two numbers - for A and B.
Answer should contain GCD and LCM for each pair, surrounded by brackets and separated by spaces, for example:

input data:
2
2 3
4 10

answer:
(1 6) (2 20)

'''

import sys


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def gcd_lcm(a, b):
    return '({} {})'.format(gcd(a, b), a * b // gcd(a, b))


n = int(input())
print(*[gcd_lcm(*list(map(int, line.rstrip().split()))) for line in sys.stdin])
