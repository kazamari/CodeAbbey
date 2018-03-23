'''
Write a program which for given N, K and I will produce I-th combination of K elements from N.

Input data will contain the amount of testcases in the first line.
Following lines will have single test-case each, formed of three values N, K and I with the following limits: N <= 36,
K <= N, 0 < I < C(N,K).
Answer should give the required combinations.

Example:

input data:
3
5 3 2
30 15 0
36 16 7307872109

answer:
014 0123456789ABCDE KLMNOPQRSTUVWXYZ
'''
from math import factorial
from sys import stdin

l = '0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()

comb = lambda n, k: int(factorial(n) / (factorial(k) * factorial(n - k)))


def nth_combination(n, k, index):
    seq, res = l[:n], []
    c = comb(n, k)
    if index < 0:
        index += c
    while k:
        c, n, k = c * k // n, n - 1, k - 1
        while index >= c:
            index -= c
            c, n = c * (n - k) // n, n - 1
        res.append(seq[-1 - n])
    return ''.join(res)


print(*[nth_combination(*map(int, line.rstrip().split())) for i, line in enumerate(stdin) if i > 0])

