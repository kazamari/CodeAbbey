'''
Your task now is simply to calculate the Levenshtein Distance between two strings. There are different algorithms, of which most popular uses dynamic programming with a table M by N (however it could be reduced to only two lines, previous and current, reassigned after each current line is completed). You can read more in the wikipedia article on Levenshtein Distance or get info from many other sources.

Input data will contain the number of test-cases in the first line.
Next lines will contain 2 "words" each - words will contain of capital latin letters only.
Answer should contain the distances for each pair of words, separated by spaces.

Example:

input data:
5
PLAIN PLAN
TREE THREE
WOMAN WOMEN
KITTEN SITTING
YPOEHOHRIWUBXMNHZF YCPOEHORIDUBXNHZF

answer:
1 1 1 3 4
'''
from sys import stdin


def lev_dist(s, t):
    if len(s) < len(t):
        return lev_dist(t, s)
    if len(t) == 0:
        return len(s)
    prev_row = range(len(t)+1)
    for i, cs in enumerate(s):
        curr_row = [i + 1]
        for j, ct in enumerate(t):
            insertions = prev_row[j + 1] + 1
            deletions = curr_row[j] + 1
            substitutions = prev_row[j] + (cs != ct)
            curr_row.append(min(insertions, deletions, substitutions))
        prev_row = curr_row
    return prev_row[-1]


print(*[lev_dist(*line.rstrip().split()) for i, line in enumerate(stdin) if i > 0])
