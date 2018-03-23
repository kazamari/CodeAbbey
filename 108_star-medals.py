'''
Input data contains the number of medals for which you are to count gems.
Next lines have a pair of values N T each.
Answer should contain the amount of gems for each of medals.

N and T will be always coprime since this allows to draw a line as a single figure - in contrast to Star of David for example which is build of two triangles.

Example:

input data:
2
5 2
7 2

answer:
5 7
'''
from sys import stdin


def gems(n, t):
    return n * (t - 1)


print(*[gems(*map(int, line.rstrip().split())) for i, line in enumerate(stdin) if i > 0])
