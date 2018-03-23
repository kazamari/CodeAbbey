'''
Suppose the "hero" is placed at some cell of hexagonal grid. Then he can move in six directions. On the picture above
X marks the initial cell and letters A, B, C, D, E, F - the possible movements for 1 step. A moves the hero directly
to the right and other directions are named in the counter-clockwise order.

You will be given a sequence of steps, performed by hero, each step described by a corresponding letter. You are to
tell after all these steps, how far the hero is now from his initial position.

We agree that the hero is always placed at the center of the cell and that distance between centers of two adjacent
cells (i.e. sharing a side) is 1.0.

Input data will contain number of test-cases in the first line.
Next lines will contain the sequence of steps (one sequence per line) as a string of letters.
Answer should contain the distances between starting and ending point for each of sequences, separated by spaces and
with accuracy of 1e-7 at least.

Example:

input data:
3
AABF
FEDCBA
BCB

answer:
3.0 0.0 2.64575131
'''
import math, sys

dirs = {'A': 0, 'B': math.pi / 3, 'C': 2 * math.pi / 3, 'D': math.pi, 'E': 4 * math.pi / 3, 'F': 5 * math.pi / 3}


def get_distance(path):
    def step(coord, direction):
        return (coord[0] + math.cos(dirs[direction]), coord[1] + math.sin(dirs[direction]))

    hero_coord = (0, 0)
    for x in list(path):
        hero_coord = step(hero_coord, x)

    return round(math.sqrt(hero_coord[0]**2 + hero_coord[1]**2), 8)


print(*[get_distance(line.rstrip()) for i, line in enumerate(sys.stdin) if i > 0])
