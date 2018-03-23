'''
The goal is to solve the equation which has the following form:

A * x + B * sqrt(x ^ 3) - C * exp(-x / 50) - D = 0

here A, B and C all would be positive so that function is monotonic. Solution is guaranteed to exist somewhere in
range 0 <= x <= 100.

Solution should be calculated with precision 0.0000001 = 1e-7 or better.

Input data will contain number of test-cases in the first line.
Next lines will contain four numbers for each test-case, i.e. A B C D separated by values.
Answer should contain solutions - i.e. values of x which satisfy equation with given coefficents - several answers
(for several test-cases) should be separated with spaces.

Example:

input data:
2
0.59912051 0.64030348 263.33721367 387.92069617
15.68387514 1.26222280 695.23706506 698.72384731

answer:
73.595368554162 41.899174957955
'''

from math import sqrt, exp
from sys import stdin

def binary_search(nums):
    A, B, C, D = map(float, nums.split())
    start, end = 0, 100
    x = 0
    for i in range(200):
        x = (start + end) / 2
        expression = A * x + B * sqrt(x ** 3) - C * exp(-x / 50) - D
        if expression == 0:
            break
        if expression < 0:
            start = x
        else:
            end = x
    return x

print(*[binary_search(line.rstrip()) for i, line in enumerate(stdin) if i > 0])

