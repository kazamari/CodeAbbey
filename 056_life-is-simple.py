'''
In this problem you will run the given configuration for 5 turns and print the number of organisms after each step.

Input data will contain 5 lines of 7 characters each. They represent a 5 by 7 fragment of the game field.
Dash characters "-" represent empty cells, while each "X" represent a cell containing a live organism.
Answer should contain 5 values separated by spaces - the amounts of live organisms after each turn.

Example:

input data:
-------
---XX--
-XXX---
-------
-------

answer:
6 5 3 2 0

# XX--XX-
# --X-X--
# X----X-
# --X--XX
# --XX-X-
#
# 22 17 24 15 12
'''
import sys


def life_step(matrix):
    n, m = len(matrix), len(matrix[0])
    def is_alive(i, j):
        neighbours = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                if not (x == 0 and y == 0):
                    neighbours += bool(matrix[(i + x) % n][(j + y) % m] == 'X')
        return (matrix[i][j] == '-' and neighbours == 3) or (matrix[i][j] == 'X' and neighbours in [2, 3])

    return [['X' if is_alive(i, j) else '-' for j in range(m)] for i in range(n)]


matrix = [list(line.rstrip().ljust(12, '-').rjust(17, '-')) for line in sys.stdin]
for _ in range(5):
    matrix.append(list('-' * 17))
    matrix.insert(0, list('-' * 17))

for _ in range(5):
    matrix = life_step(matrix)
    print(sum([x.count('X') for x in matrix]), end=" ")
