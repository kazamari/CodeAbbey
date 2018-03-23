'''
Input data will have:

    initial integer number in the first line;
    one or more lines describing operations, in form sign value where sign is either + or * and value is an integer;
    last line in the same form, but with sign % instead and number by which the result should be divided to get the
    remainder.

Answer should give remainder of the result of all operations applied sequentially (starting with initial number)
divided by the last number.

If you have troubles with this problem, please feel free to type its name in the "Search" box in the top menu and find
relevant topics at our forum - probably you will get enough enlightenment from there.

Example:

input data:
5
+ 3
* 7
+ 10
* 2
* 3
+ 1
% 11

answer:
1

In this case result after all operations applied sequentially is 397.

All numbers will not exceed 10000 (though intermediate results could be very large).
'''

import sys

n = 0

for i, line in enumerate(sys.stdin):
    line = line.rstrip()
    if i == 0:
        n = int(line)
    else:
        op, num = line.split()
        if op == '+':
            n += int(num)
        elif op == '*':
            n *= int(num)
        elif op == '%':
            n %= int(num)

print(n)
