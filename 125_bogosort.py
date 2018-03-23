'''
Input data will contain the number of test-cases in the first line.
Each testcase given in separate line will contain an array of exactly 7 values.
Answer should contain the amount of shuffles needed to sort the given array or -1 if it will never be sorted.

Example:

input data:
4
61 91 35 135 105 120 161
156 30 119 99 81 60 137
102 170 142 55 117 83 26
102 81 128 168 56 145 27

answer:
-1 156 -1 1391

Note: random generator should be reinitialized for each test!
'''
from sys import stdin


def rnd(seed):
    x = str(seed).zfill(6)
    y = int(x[3:]+x[:3])
    return int(str(seed * y).zfill(12)[3:-3])


def is_sorted(a):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return False
    return True


def bogosort(a):
    iters, r, n = 0, 918255, len(a)
    sorted_a = a[:]
    while not is_sorted(sorted_a):
        for i in range(n):
            r = rnd(r)
            j = r % n
            sorted_a[i], sorted_a[j] = sorted_a[j], sorted_a[i]
        if a == sorted_a:
            return -1
        iters += 1
    return iters


print(*[bogosort(list(map(int, line.rstrip().split()))) for i, line in enumerate(stdin) if i > 0])

