'''
You are given a set of items - their weights and values. Also you are told the maximum total weight (capacity of the
knapsack). Return the maximum possible value of chosen items.

Input data will contain amount of items N on the first line.
Next line will have the maximum allowed capacity Wmax of the knapsack.
Then there would be N lines each with two values - w[i] and v[i].
Answer should have a single value - maximum posible value of items placed into knapsack.

Example:

input data:
7
86
5 8
15 20
13 25
15 31
28 65
8 14
23 57

answer:
186

Here items with values 8, 25, 31, 65 and 57 are choosen with total weight of 84.
'''
from sys import stdin


def solve_knapsack(wmax, items):
    n = len(items)
    K = [[0 for x in range(wmax + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(wmax + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif items[i - 1][0] <= w:
                K[i][w] = max(items[i - 1][1] + K[i - 1][w - items[i - 1][0]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][wmax]


given = [line.rstrip() for line in stdin]

N, W_max = map(int, given[:2])
items = [list(map(int, line.split())) for line in given[2:]]

print(solve_knapsack(W_max, items))
