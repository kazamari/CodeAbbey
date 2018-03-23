from sys import stdin

a, b = 6, 5
dunge = [
    ['@', '+', '+', '+', '+'],
    ['+', '+', '+', 'X', 'X'],
    ['+', 'X', '+', '+', '+'],
    ['+', '+', '+', 'X', '+'],
    ['+', 'X', '+', '+', 'X'],
    ['+', '+', '+', '+', '$']
]

dunge[a-1][b-1]=1

print(dunge)

for y in reversed(range(a)):
    for x in reversed(range(b)):
        print(y, x, dunge)
        if dunge[y][x] == "X" or x + y == a + b - 2:
            continue
        down = (dunge[y + 1][x] if y + 1 < a and dunge[y + 1][x] != 'X' else 0)
        right = (dunge[y][x + 1] if x + 1 < b and dunge[y][x + 1] != 'X' else 0)
        dunge[y][x] = down+right
print(dunge[0][0])


# grid = []
#
# for i, line in enumerate(stdin):
#     if i == 0:
#         m, n = map(int, line.rstrip().split())
#     else:
#         grid.append(line.rstrip().split())