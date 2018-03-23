'''
You will be given the array for which checksum should be calculated. Perform calculation as follows: for each element
of the array (starting from beginning) add this element to result variable and multiply this sum by 113 - this
new value taken by modulo 10000007 should become the next value of result, and so on.

Input data will tell the length of an array in the first line.
Array values themselves follow in the second line, separated by spaces.
Answer should have a single value - calculated checksum.

Example:

input data:
6
3 1 4 1 5 9

answer:
8921379

All input values are between 0 and 1,000,000,000 - be sure to take care of possible overflow in progress of calculations!
'''

def check_sum(list):
    sum = 0
    for x in list:
        sum = (sum + x) * 113
    return sum % 10000007

n = int(input())
print(check_sum(map(int, input().split())))
