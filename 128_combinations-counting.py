'''
How many combinations of K elements from the set of N exist (assuming all N elements are different). It could be easily
found that the math formula is:

      N!
------------- = C(N, K) - the number of different combinations
K! * (N - K)!

Where X! is the factorial of X, i.e. product 1 * 2 * 3 * ... * X.
Problem statement

You are to calculate exactly this value C(N, K) for given N and K. Note that though some languages (Python and Java for
example) have built-in long arithmetics, it would be good if you'll find a way to minimize intermediate results in
calculations. It would be crucial for C/C++ sometimes.

If it is too simple for you, please try to write program for Enumerating Combinations task!

Input data will contain the amount of test-cases.
Next lines will contain one test-case each in form of two values (N K).
Answer should contain C(N, K) for each case.

Example:

input data:
3
3 0
4 2
5 2

answer:
1 6 10

Note: results would be small enough for storing in 64-bit integers.
'''

from math import factorial
from sys import stdin

c = lambda n, k: int(factorial(n) / (factorial(k) * factorial(n-k)))

print(*[c(*map(int, line.rstrip().split())) for i, line in enumerate(stdin) if i > 0])

# We can rewrite the given formula:
#
# C(N, K) = N/1 * (N-1)/2 * ...
#    ... * (N-K+2)/(K-1) * (N-K+1)/K
#
# and the proper way to minimize intermediate results is to calculate the result in exactly this order - multiply, divide,
# multiply, divide... It is up to you to show that non-integer results could not be encountered in this manner :)

#
# def c(n, k):
#     cnk = 1
#     for i in range(1, k + 1):
#         cnk *= (n - i + 1) / i
#     return int(cnk)
#
#
# print(*[c(*map(int, line.rstrip().split())) for i, line in enumerate(stdin) if i > 0])




