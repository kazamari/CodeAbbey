'''
Input data will contain the amount of values to convert in the first line.
Other lines will contain one value each, in form like 0.142857.
Answer should contain numbers from 1 to 6 for each of input values, produced by the discussed algorithm.

Example:

6
0.59558786964
0.861037873663
0.385597702116
0.246237673331
0.808033385314
0.0544673665427

answer:
4 6 3 2 5 1

'''

import sys

def dice(n):
    return int(n * 6 + 1)

n = int(input())
print(*[dice(float(line.rstrip())) for line in sys.stdin])