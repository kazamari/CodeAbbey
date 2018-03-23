'''
Input data will contain number of stocks (share types or names) for which calculations should be done.
Next lines contain descriptions of stock - the stock name (four latin letters) and then 14 values - prices for each day
over last fortnight.
Answer should contain names of stocks which are volatile enough by Paul's criteria (in the same order as they were given
in the input).

Example:

input data:
2
JOOG 99 99 99 99 99 99 99 101 101 101 101 101 101 101
GOLD 95 105 95 105 95 105 95 105 95 105 95 105 95 105

answer:
GOLD
'''
from math import sqrt
from sys import stdin


def deviation(stock, comission):
    name, prices = stock.split(' ', 1)
    prices = list(map(int, prices.split()))
    n = len(prices)
    mean = sum(prices) / n
    deviation = sqrt(sum([(x - mean)**2 for x in prices]) / n)
    return deviation / (mean * comission * 0.01) >= 4


print(*[x[:4] for x in [line.rstrip() for i, line in enumerate(stdin) if i > 0] if deviation(x, 1)])
