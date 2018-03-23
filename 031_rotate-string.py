'''
Input data will contain the number of test-cases in the first line.
Following lines will contain number K and some string S separated by space - one pair in each line.
String S will contain only small latin letters. K will not exceed half the length of S by absolute value.
Answer should contain strings rotated in accordance with the rule above, separated by spaces. For example:

input data:
2
3 forwhomthebelltolls
-6 verycomplexnumber

answer:
whomthebelltollsfor numberverycomplex

The task could be easily solved by creating new instance of string concatenating two substrings. However, if you want
more serious challenge, you are encouraged to perform rotation "in-place", moving bytes of original string
(i.e. without allocating memory for new instance). This could be done with the help of a loop and only one temporary
variable.
'''

import sys


def rotate(*args):
    k, l = int(args[0]), list(args[1])
    for i in range(abs(k)):
        if k > 0:
            ch = l.pop(0)
            l.append(ch)
        elif k < 0:
            ch = l.pop(-1)
            l.insert(0, ch)
    return ''.join(l)


print(*[rotate(*line.rstrip().split()) for i, line in enumerate(sys.stdin) if i > 0])
