init = [
            [2, 2, 4, 2],
            [4, 2, 2, 4],
            [2, 2, 2, 2],
            [2, 4, 2, 2],
        ]


def move(self, direction):
    merged = []
    moved = False
    lines = rotate(self.grid, direction + 1)
    for line in lines:
        while len(line) and line[-1].value == 0:
            line.pop(-1)
        i = len(line) - 1
        while i >= 0:
            if line[i].value == 0:
                moved = True
                line.pop(i)
            i -= 1
        i = 0
        while i < len(line) - 1:
            if line[i].value == line[i + 1].value and not (line[i] in merged or line[i + 1] in merged):
                moved = True
                line[i] = Tile(line[i].value * 2)
                merged.append(line[i])
                line.pop(i + 1)
            else:
                i += 1
        while len(line) < len(self.grid):
            line.append(Tile())
    for line in lines:
        if not len(lines):
            line = [Tile() for i in self.grid]
    self.grid = rotate(lines, 0 - (direction + 1))
    if moved:
        self.addRandomTile()