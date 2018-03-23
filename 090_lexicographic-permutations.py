'''
For example, if there were only 4 letters, then 24 permutations exist and if placed in order they'll look like:

 0 ABCD     1 ABDC     2 ACBD     3 ACDB     4 ADBC     5 ADCB
 6 BACD     7 BADC     8 BCAD     9 BCDA    10 BDAC    11 BDCA
12 CABD    13 CADB    14 CBAD    15 CBDA    16 CDAB    17 CDBA
18 DABC    19 DACB    20 DBAC    21 DBCA    22 DCAB    23 DCBA

And if Geeglo is told that first 9 of them were already tried, he should proceed from BCDA.

Input data contain the number of test-cases in the first line.
Next lines contain a single value each - the number of permutations tried by unknown monk.
Answer should contain the same amount of letter permutations - ones with which Geeglo should start in each case.

Example:

input data:
3
0
2
10531100

answer:
ABCDEFGHIJKL ABCDEFGHIKJL ADLBEHICKGFJ
'''
from math import factorial, floor
from sys import stdin


def nth_perm(s, n):
    perm = []
    while s != []:
        f = factorial(len(s) - 1)
        i = int(floor(n / f))
        n %= f
        perm.append(s[i])
        s = s[:i] + s[i+1:]
    return ''.join(perm)


s = 'ABCDEFGHIJKL'
print(*[nth_perm(list(s), int(line.rstrip())) for i, line in enumerate(stdin) if i > 0])