'''
Input data will contain the length of the sequence in the first line.
The second line will contain the measurements itself.
Answer should contain the processed sequence. All values should be calculated to precision of 1e-7 or better.

Example:

input data:
7
32.6 31.2 35.2 37.4 44.9 42.1 44.1

answer:
32.6 33 34.6 39.1666666667 41.4666666667 43.7 44.1
'''

n = int(input())
list = list(map(float, input().split()))
print(*[(list[i-1] + list[i] + list[i+1]) / 3 if 1 <= i <= n-2 else list[i] for i in range(n)])
