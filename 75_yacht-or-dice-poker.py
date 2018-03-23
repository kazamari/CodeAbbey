'''
Dice game of Yacht is played with 5 standard dice (having from 1 to 6 points on their sides). The player's goal is to
gather some beautiful combination of points. Suppose, the following combinations are respected:

    two of dice have the same points, like 3 6 5 6 1 - called pair;
    three of dice have the same points, like 2 4 5 4 4 - called three;
    four of dice have the same points, like 1 4 1 1 1 - called four;
    all five dice have the same points, like 2 2 2 2 2 - called yacht;
    two pairs at once, like 3 6 5 3 5 - called two-pairs;
    pair and three at once, like 1 6 6 1 6 - called full-house;
    sequence from 1 to 5, like 2 4 3 5 1 - called small-straight;
    sequence from 2 to 6, like 6 3 4 2 5 - called big-straight.

(combinates named with two words are written with dash here for consistency with answers which our code will produce)

Such combinations increases player's score by different values, but it is not important now.

Our goal is to write a program which for given combination of dice will determine its type.

Input data contains a number of test-cases in the first line.
Next lines contain 5 values each - points of player's dice.
Answer should contain the name for each of combinations. Names could be pair, two-pairs, three, four, yacht, full-house,
small-straight, big-straight or none, separated with spaces.

Example:

input data:
3
3 6 5 6 1
1 6 6 1 6
2 4 3 5 1

answer:
pair full-house small-straight
'''
import sys


def dice_poker(dice):
    q = sorted({x: dice.count(x) for x in dice}.values(), reverse=True)
    if q[0] == 5:
        return 'yacht'
    if q[0] == 4:
        return 'four'
    if q[0] == 3:
        if q[1] == 2:
            return 'full-house'
        return 'three'
    if q[0] == 2:
        if q[0] == q[1]:
            return 'two-pairs'
        return 'pair'
    if len(q) == 5:
        if sorted(dice)[0] == '1':
            return 'small-straight'
        if sorted(dice)[0] == '2':
            return 'big-straight'


print(*[dice_poker(line.rstrip().split()) for i, line in enumerate(sys.stdin) if i > 0])

