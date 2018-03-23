'''
Input data will have the number of test-cases in the first line.
Next lines will contain three values each S A B.
Answer should contain the distances between first city and rendezvous point (i.e. distance travelled by first cyclist
before they meet), separated with spaces.

Example:

input data:
2
10 1 1
20 1 2

answer:
5 6.66666667

Note: the floating point values should have precision 10e-7 or better
'''

import sys
n = int(input())

for line in sys.stdin:
    s, a, b = map(float, line.rstrip().split())
    print((a * s) / (a + b), end=" ")
