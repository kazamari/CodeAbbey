'''
Input data contain number of test-cases in the first line.
Then the specified number of lines follows each representing one test-case.
Lines consist only of lowercase English (Latin) letters and spaces.
Answer should contain the number of vowels in each line, separated by spaces.

Example:

input data:
4
abracadabra
pear tree
o a kak ushakov lil vo kashu kakao
my pyx

answer:
5 4 13 2

'''

import sys

print(*[len([x for x in line if x in 'aouiey']) for i, line in enumerate(sys.stdin) if i > 0])
