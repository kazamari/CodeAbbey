'''
Input data are in the following format:

    first line contains N - the number of values to process;
    and then N lines will follow describing the values for which sum of digits should be calculated by 3 integers A B C;
    for each case you need to multiply A by B and add C (i.e. A * B + C) - then calculate sum of digits of the result.

Answer should have N results, also separated by spaces. For example:

input data:
3
11 9 1
14 90 232
111 15 111

answer:
1 16 21

Here the first case requires to calculate 11*9+1 = 100 and its sum of digits is 1+0+0 = 1.
'''

import sys

def sum_of_digits(n):
    a, b = n // 10, n % 10
    res = b
    while a >= 10:
        b, a = a % 10, a // 10
        res += b
    return res + a

n = int(input())
for line in sys.stdin:
    a, b, c = map(int, line.rstrip().split())
    print(sum_of_digits(a * b + c), end=" ")
