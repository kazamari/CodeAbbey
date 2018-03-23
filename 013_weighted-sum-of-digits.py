'''
This program resembles more complex algorithms for calculation CRC and other checksums and also hash-functions on
character strings. Besides it will provide you with one more exercise on splitting values to decimal digits.
You may want to try Sum of Digits before this one.

Let us calculate sum of digits, as earlier, but multiplying each digit by its position (counting from the left,
starting from 1). For example, given the value 1776 we calculate such weighted sum of digits (let us call it "wsd") as:

wsd(1776) = 1 * 1 + 7 * 2 + 7 * 3 + 6 * 4 = 60

Input data will give the number of test-cases in the first line.
Values themselves are in the second line. For each of these values you are to calculate weighted sum of digits.
Answer: as usually, put results in one line, separating them with spaces.

Example:

input data:
    3
    9 15 1776

answer:
    9 11 60
'''

def wsd(num):
    l, res = [], num
    while res > 0:
        l.insert(0, res % 10)
        res = res // 10
    return sum([l[i] * (i + 1) for i in range(len(l))])

n = int(input())
print(*[wsd(x) for x in map(int, input().split())])
