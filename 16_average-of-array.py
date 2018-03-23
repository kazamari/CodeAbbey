'''
Input data will give the number of test-cases in the first line.
Then test-cases themselves will follow, one case per line.
Each test-case describes an array of positive integers with value of 0 marking end. (this zero should not be included into calculations!!!).
Answer should contain average values for each array, rounded to nearest integer (see task on rounding), separated by spaces.

Example:

input data:
3
2 3 7 0
20 10 0
1 0

answer:
4 15 1

'''

import sys


def round_to_int(n):
    return int(n+0.5) if n-int(n) == 0.5 else round(n)


def av(s):
    l = list(map(int, s.split()[:-1]))
    return round_to_int(sum(l)/len(l))


print(*[av(line.rstrip()) for i, line in enumerate(sys.stdin) if i > 0])
