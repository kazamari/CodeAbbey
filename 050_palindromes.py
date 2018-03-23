'''
Input data contains number of phrases in the first line.
Next lines contain one phrase each.
Answer should have a single letter (space separated) for each phrase: Y if it is a palindrome and N if not.

Example:

input data:
3
Stars
O, a kak Uwakov lil vo kawu kakao!
Some men interpret nine memos

answer:
N Y Y
'''

from re import sub
from sys import stdin


def is_palindrome(s):
    s = sub(r'\W', '', s.lower())
    return 'Y' if s == s[::-1] else 'N'


print(*[is_palindrome(line.rstrip()) for i, line in enumerate(stdin) if i > 0])
