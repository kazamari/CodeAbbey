'''
Input data will give a number of test-cases in the first line.
Next lines will contain one test-case (i.e. the pair of numbers) each.
Answer should contain division-and-rounding results for each pair, separated with spaces

Example:

input data:
3
12 8
11 -3
400 5

answer:
2 -4 80

'''

import sys
def round_to_int(n):
    return int(n+0.5) if n-int(n) == 0.5 else round(n)

n, res = 0, []
for i, line in enumerate(sys.stdin):
    line = line.rstrip()
    if i == 0:
        n = int(line)
    else:
        a, b = map(float, line.split())
        res.append(round_to_int(a / b))

print(*res)
