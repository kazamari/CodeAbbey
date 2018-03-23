'''
In this problem you need to write a program which for given value of s = a + b + c will find the only triple which
satisfies the equation.

For example, given sum of 12 the only 3, 4, 5 triple fits, for sum 30 the only 5, 12, 13 etc.

Input data will contain the number of test-cases in the first line.
Other lines will contain a single value each - the sum for which triple should be found.
Answer should contain the values of c^2 for each triple found (it is equal to a^2 + b^2 of course), separated with spaces.

Note: the real values of s would be large enough, about 10e+7 - so the simplest solutions could be inefficient.

Example:

input data:
2
12
30

answer:
25 169
'''
from sys import stdin


def pyth_c(s):
    for a in range(2, s):
        if (s * s - 2 * s * a) % (2 * s - 2 * a) == 0:
            b = (s * s - 2 * s * a) // (2 * s - 2 * a)
            c = s - a - b
            if c > 0 and a**2 + b**2 == c**2:
                return c**2


print(*[pyth_c(int(line.rstrip())) for i, line in enumerate(stdin) if i > 0])