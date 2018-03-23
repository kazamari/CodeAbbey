'''
Input data: First line will contain number of triplets.
Other lines will contain triplets themselves (each in separate line).
Answer: You should output 1 or 0 for each triplet (1 if triangle could be built and 0 otherwise).

Example:

data:
2
3 4 5
1 2 4

answer:
1 0

'''

from sys import stdin

def is_triangle(triplet):
    a, b, c = sorted(triplet)
    return int(c <= a + b)

print(*[is_triangle(map(int, line.rstrip().split())) for i, line in enumerate(stdin) if i > 0])
