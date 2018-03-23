'''
Now all you need to do is a calculation of raising A to power of B with result taken by modulo M.

This operation is the cornerstone of many algorithms like generation of probable primes, generating keys for modern cryptography etc.

Though some languages have built-in functions for such calculation, of course it would be better for you to find another approach!

Input data will contain the number of testcases in the first line.
Next lines will have three values for A B M each.
Answer should give (A^B)%M for each case.

Example:

input data:
3
14 28 219431273
30 56 351887801
43 47 289907803

answer:
5022695 292780914 140818938
'''
from sys import stdin


def modexp(y, x, m):
    a, b, c = x, 1, y
    while a != 0:
        if a % 2 == 0:
            a = a/2
            c = (c**2) % m
        else:
            a = a -1
            b = (b * c) % m
    return b


print(*[modexp(*map(int, line.rstrip().split())) for i, line in enumerate(stdin) if i > 0])
