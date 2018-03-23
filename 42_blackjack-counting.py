'''
The game of Blackjack has very simple rules: players should take cards one by one trying to collect more points than
opponents, but not exceeding 21 (refer Wikipedia for complete rules).

The deck contains all cards from 2 to 10 inclusive, which are counted according to their value, also Kings, Queens and
Jacks which cost 10 points each and also Aces, which could be counted as 1 or 11 points, whatever is better.

Let us learn the programming of scoring algorithm for such game.

Input data will contain the number of test-cases in the first line.
Then test-cases will follow on separate lines. Each test-case consists of several cards expressed with symbols:
2, 3, 4, 5, 6, 7, 8, 9,
T, J, Q, K - for 10, Jack, Queen, King,
A - for Ace.
Answer should contain the number of points in each test-case, not exceeding 21 - or the word Bust if the total is
greater than 21 (i.e. player immediately loss).

Example:

input data:
4
A T
2 K 4
3 A Q 8
A 3 3 3 A

answer:
21 16 Bust 21
'''
import sys


def blackjack(s):
    sum = 0
    for x in sorted(s.split(), key=lambda x: 1 if x == 'A' else 0):
        if x.isdigit():
            sum += int(x)
        elif x != 'A':
            sum += 10
        else:
            sum += 11 if (21 - sum) >= 11 else 1
    return sum if sum <= 21 else 'Bust'


print(*[blackjack(line.rstrip()) for i, line in enumerate(sys.stdin) if i > 0])
