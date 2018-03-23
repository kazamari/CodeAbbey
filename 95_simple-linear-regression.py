'''
You will be given a list of records, each containing the number of rainy days during previous year along with the
average price for which the wine was sold during current year.

Use the Simple Linear Regression and criteria of the Ordinary Least Squares to find parameters of the linear function
which can approximate the dependence between price and amound of rainy days.

Input data contains starting A and ending B year in the first line.
Then lines follow for each year in form YYYY: D P where YYYY is the mark of year, D is the number of rainy days
(in previous season) and P is the wine price (in crowns per barrel).
Answer should contain values for K and B with accuracy of 1e-7 or better.

Example:

input data:
1925 1947
1925: 89 257
1926: 75 226
1927: 83 235
1928: 52 173
1929: 148 332
1930: 109 268
1931: 129 306
1932: 115 289
1933: 102 265
1934: 99 269
1935: 50 228
1936: 102 265
1937: 91 256
1938: 79 238
1939: 118 298
1940: 134 311
1941: 61 155
1942: 146 340
1943: 108 274
1944: 96 242
1945: 89 232
1946: 143 328
1947: 133 303

answer:
1.54053779316 107.312854273
'''
from sys import stdin


def regression(array):
    n = len(array)
    X = sum([x for x, y in array])
    Y = sum([y for x, y in array])

    A = sum([xi**2 for xi, yi in array])
    C = sum([xi*yi for xi, yi in array])

    D = X**2 - n*A
    k = (X*Y - n*C) / D
    b = (C*X - A*Y) / D

    return k, b


l = [list(map(int, line.rstrip().split()[1:])) for i, line in enumerate(stdin) if i > 0]
print(*regression(l))
