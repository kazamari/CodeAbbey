'''
So you are given values for A and B and your goal is to find x satisfying the equation.

Input data will contain the number of test-cases in the first line.
Each case in the separate lines consists of three values M A B.
Answer should give value x for each case or -1 (not valid value) if modular inverse could not be calculated (due to A
and M not being coprime).

Example:

input data:
3
71 10 29
57 42 31
36 17 24

answer:
61 -1 24
'''
from sys import stdin


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def egcd(a, b):
    s1, s2, t1, t2 = 1, 0, 0, 1
    while b > 0:
        s1, s2 = s2, s1 - (a // b) * s2
        t1, t2 = t2, t1 - (a // b) * t2
        a, b = b, a % b
    return a, s1, t1


def get_x(M, A, B):
    if gcd(A, M) == 1:
        g, a, b = egcd(A, M)
        if a < 0:
            a += M
        return (-B * a) % M
    else:
        return -1


print(*[get_x(*map(int, line.rstrip().split())) for i, line in enumerate(stdin) if i > 0])
