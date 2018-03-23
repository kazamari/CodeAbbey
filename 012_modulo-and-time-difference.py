'''
Input data: the first line contains number of test-cases, other lines contain test-cases themselves.
Each test-case contains 8 numbers, 4 for each timestamp: day1 hour1 min1 sec1 day2 hour2 min2 sec2 (second timestamp
will always be later than first).
Answer: for each test-case you are to output difference as following (days hours minutes seconds) - please note
brackets - separated by spaces.

Example:

input data:
3
1 0 0 0 2 3 4 5
5 3 23 22 24 4 20 45
8 4 6 47 9 11 51 13

answer:
(1 3 4 5) (19 0 57 23) (1 7 44 26)

'''

from sys import stdin


def get_diff(times_line):
    to_sec = lambda d, h, m, s: s + 60 * (m + 60 * (h + 24 * d))
    d1, h1, m1, s1, d2, h2, m2, s2 = map(int, times_line.split())
    diff = to_sec(d2, h2, m2, s2) - to_sec(d1, h1, m1, s1)
    s = diff % 60
    diff //= 60
    m = diff % 60
    diff //= 60
    h = diff % 24
    d = diff // 24
    return '({} {} {} {})'.format(d, h, m, s)


print(*[get_diff(line.rstrip()) for i, line in enumerate(stdin) if i > 0])
