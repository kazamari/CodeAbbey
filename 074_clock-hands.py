'''
Input data contain the number of test cases.
Following line contains the testcases themselves in form 3:15, 21:44 etc.
Answer should contain four real numbers for each test case - X and Y coordinates for hour hand, then X and Y coordinate
for minute hand. All values should be simply separated with spaces.

Real values should have accuracy of 1e-7 or better. Time is specified as a value from 0:00 to 23:59.

Example:

input data:
3
12:00 15:00 9:30

answer:
10.0 16.0 10.0 19.0 16.0 10.0 10.0 19.0 4.20444504 11.55291427 10.0 1.0
'''
import math

ugol_min_min = 360 / 60
ugol_chas_min = 360 / 12 / 60
l_h = 6
l_m = 9


def deg_to_rad(deg):
    return deg/360*math.pi*2


def clock_coord(time):
    h, m = map(int, time.split(':'))

    a_chas = deg_to_rad((h % 12) * (360 / 12) + m * ugol_chas_min)
    a_min = deg_to_rad(m * ugol_min_min)

    return ' '.join(map(str, [math.sin(a_chas) * l_h + 10, math.cos(a_chas) * l_h + 10, math.sin(a_min) * l_m + 10, math.cos(a_min) * l_m + 10]))


n = int(input())
print(*[clock_coord(time) for time in input().split()])
