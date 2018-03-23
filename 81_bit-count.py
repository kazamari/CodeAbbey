'''
If the problem would include only positive numbers it was just the same as calculating sum of digits for binary value.

However with negative numbers present, the best way is to use bit operations - read about them for your favorite
language. The typical solution may look like:

    while the value is not 0
    test the least bit for being 1 and increment counter if it is so;
    logically shift right by 1 bit.

Note that in some languages there are both logic and arithmetic right shift, and the second will not be handy, so you
may prefer shifting to left and testing for highest bit.

For example in Python this may look like:

def count_bits(x):
    c = 0
    for i in range(32):
        c += (x & 1)
        x >>= 1
    return c

For example:

value             binary                count
  1   00000000000000000000000000000001      1
100   00000000000000000000000001100100      3
 -1   11111111111111111111111111111111     32

Input data will contain a number of values to process.
Next line will contain the values themselves, each in range -2 000 000 000 .. 2 000 000 000.
Answer should contain the counts of bits set to 1 for each of values, separated by spaces.

Example:

input data:
3
1 100 -1

answer:
1 3 32
'''

n = int(input())

print(*[bin(x % 0x100000000).count('1') for x in map(int, input().split())])

