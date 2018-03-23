'''
So here is a small programming problem without the problem statement.

Example:

input data:
5
1 2
1 2 3
2 3 4
2 4 6 8 10
7 11 19

answer:
5 14 29 220 531
'''

from sys import stdin

print(*[sum([int(x)**2 for x in line.rstrip().split()]) for i, line in enumerate(stdin) if i > 0])