'''
You will be given several records of the played games. You are to tell for each of them who of players won.

Input data will contain the number of matches played in the first line.
Then the matches description is written in separate lines.
Each line contain several pairs of letters, like PR (first casts Paper, second casts Rock), or SS (both cast Scissors),
separated with spaces.
Answer should for each of matches specify whether first player wins (by value 1) or second (by value 2). There would be
no draws.

Example:

input data:
3
SS PR
PR RS PS PP SP
PS RR PS RP

answer:
1 1 2
'''
import sys


def winner(match):
    dict = {1: 0, 2: 0}

    for g1, g2 in map(list, match):
        if g1 != g2:
            if (g1 == 'S' and g2 != 'R') or (g1 == 'P' and g2 != 'S') or (g1 == 'R' and g2 != 'P'):
                dict[1] += 1
            else:
                dict[2] += 1

    return sorted(dict.items(), key=lambda x: x[1], reverse=True)[0][0]


print(*[winner(line.rstrip().split()) for i, line in enumerate(sys.stdin) if i > 0])
