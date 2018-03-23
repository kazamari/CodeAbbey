'''
Input data will contain the number of test-cases in the first line.
Next lines will contain a single word each.
Answer should contain the number of anagrams for each word (not including the word itself).

Example:

input data:
3
bat
coal
lots

answer:
1 1 2
'''

import sys

with open('words.txt', 'r') as f:
    words = [line.rstrip() for line in f]

print(*[len([x for x in words if sorted(x) == sorted(word.rstrip()) and word.rstrip() != x]) for i, word in enumerate(sys.stdin) if i > 0])