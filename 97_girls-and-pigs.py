'''
The girls are pasturing pigs at the field. In total they have 106 legs and 336 breasts. How many girls and pigs are there?

Input data will have the number of testcases in the first line.
Next lines will contain a pair of values each - the amounts of legs and breasts - the first of them will always be
smaller than the second.
Answer should give the amount of solutions for each case.

Example:

input data:
4
6 10
26 136
106 336
200 500

answer:
1 2 3 9

Note: of course we assume that all pigs have the same number of breasts because they are of the same breed - otherwise
the problem will become senseless. We also assume this number is even for pigs (as for most mammals), though not limited
from the top.

Explanation

For the input data 26 and 136 possible solutions are:

    5 pigs with 26 breasts each (giving 20 legs and 130 breasts) with 3 girls;
    1 pig with 114 breasts (mega-pig!) under the care of 11 girls.
'''
from sys import stdin


def girls_pigs(legs, tits):
    res = []
    for z in range(6, tits - legs + 6, 2):
        y = (tits - legs) / (z - 4)
        if y.is_integer():
            x = (legs - 4 * y) / 2
            if x > 0:
                res.append([x, y, z])
    return res


print(*[len(girls_pigs(*map(int, line.rstrip().split()))) for i, line in enumerate(stdin) if i > 0])