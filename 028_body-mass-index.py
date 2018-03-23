'''
Input data contain number of people in the first line.
Other lines will contain two values each - weight in kilograms and height in metres.
Answer should contain words under, normal, over, obese for each corresponding test-case, separated with spaces. For example:

input data:
3
80 1.73
55 1.58
49 1.91

answer:
over normal under
'''

import sys

def text(bmi):
    if bmi < 18.5:
        return 'under'
    elif 18.5 <= bmi < 25.0:
        return 'normal'
    elif 25.0 <= bmi < 30.0:
        return 'over'
    elif bmi >= 30.0:
        return 'obese'

n = int(input())
for line in sys.stdin:
    m, l = map(float, line.rstrip().split())
    print(text(m / (l ** 2)), end=" ")
