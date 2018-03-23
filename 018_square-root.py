'''

    Let us search for square root r of the given value X.
    Use some arbitrary value, say r = 1 as the first approximation (surely it is too rough).
    For proper square root the equation r = X / r should hold.
    So let us calculate d = X / r (it would not be equal to r since r is not precise root).
    And take average between r and d as the new approximation.

E.g. overall formula of the calculation step is (here := is an assignment):

      r  +  X / r
r := -------------
           2

Refer to Square Root Approximation article for more details on the Heron's Method.

So we are given values X for which to perform calculations and number of steps N to perform.
Use r = 1 at the beginning, and output resulting approximation (after N steps).

Input data will give the number of test-cases in first line.
Next lines will contain test-cases themselves, each containing the value X for which square root should be calculated
and N - the number of calculation steps.
Answer should contain calculated approximations for each case, separated by space.

Example:

input data:
3
150 0
5 1
10 3

answer:
1 3 3.196

Results should have precision of 1e-7 = 0.0000001 or better!
'''

from sys import stdin


def root(x, n):
    r = 1
    for i in range(n):
        r = (r + x / r) / 2
    return r


print(*[root(*map(int, line.rstrip().split())) for i, line in enumerate(stdin) if i > 0])
