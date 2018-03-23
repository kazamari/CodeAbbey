import sys

w = h = 5
score = 0
box = [[] for _ in range(w)]

for line in sys.stdin:
    for i, x in enumerate(map(int, list(line.rstrip()))):
        box[i].insert(0, x)

for row in box:
    print(*row)

def remove(x, y):
    global score, box, w, h
    c = box[x][y]
    cells = [(x, y)]
    count = 0
    minx = maxx = x
    while len(cells) > 0:
        cur = cells.pop()
        print(box[cur[0]][cur[1]])
        count += 1
        box[cur[0]][cur[1]] = 0
        minx = min(minx, cur[0])
        maxx = max(maxx, cur[0])
        if cur[0] > 0 and box[cur[0] - 1][cur[1]] == c:
            cells.append((cur[0] - 1, cur[1]))
        if cur[1] > 0 and box[cur[0]][cur[1] - 1] == c:
            cells.append((cur[0], cur[1] - 1))
        if cur[0] < w - 1 and box[cur[0] + 1][cur[1]] == c:
            cells.append((cur[0] + 1, cur[1]))
        if cur[1] < h - 1 and box[cur[0]][cur[1] + 1] == c:
            cells.append((cur[0], cur[1] + 1))
    for x in range(minx, maxx+1):
        col = []
        for y in range(h):
            c = box[x][y]
            if c > 0:
                col.append(c)
        while len(col) < h:
            col.append(0)
        box[x] = col
    for xx in range(w - 1, -1, -1):
        if box[xx][0] == 0:
            col = box[xx]
            box.pop(xx)
            box.append(col)
    score += count * (count + 1) / 2
    for row in box:
        print(*row)

for x, y in [map(int, s.split()) for s in '0 4, 3 0, 0 1, 2 2, 1 1, 4 2, 3 2, 0 1, 3 2, 3 1, 3 0, 2 0'.split(', ')]:
    remove(x, y)

print(score)
