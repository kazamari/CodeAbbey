'''
You will be given several numbers (not very large, so do not be afraid) to decompose them into products of primes.

Input data will contain amount of integers to factorize in the first line.
Next lines will contain one integer each (not exceeding 13 digits in length).
Answer should contain product representation for each of these integers, written like p1*p2*p3 where p1 ... p3 are some primes sorted in non-decreasing order. Products should be separated with spaces.

Example:

input data:
5
1000
1001
1002
1003
1009

answer:
2*2*2*5*5*5 7*11*13 2*3*167 17*59 1009
'''

import sys


def factorize(n):
    def isPrime(n):
        return not [x for x in range(2, int(n ** 0.5) + 1) if n % x == 0]

    primes = []
    candidate = 2
    while not primes and candidate in range(2, n+1):
        if n % candidate == 0 and isPrime(candidate):
            primes = primes + [candidate] + factorize(n // candidate)
        candidate += 1
    return primes


print(*['*'.join(map(str, factorize(int(line.rstrip())))) for i, line in enumerate(sys.stdin) if i > 0])

