'''
Input data: first line contains the number of test-cases.
Other lines contain test-cases in form of triplets of values A B N where A is the first value of the sequence,
B is the step size and N is the number of first values which should be accounted.

Answer: you are to output results (sums of N first members) for each sequence, separated by spaces.

Example:

data:
2
5 2 3
3 0 10

answer:
21 30

'''

from sys import stdin

def sum_progression(a, b, n):
    return int(((2 * a + b * (n - 1)) / 2) * n)

print(*[sum_progression(*map(int, line.rstrip().split())) for i, line in enumerate(stdin) if i > 0])
