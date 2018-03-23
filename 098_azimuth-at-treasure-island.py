'''
Input data will be in format close to the directions inscribed on a map:
The first line contains words Stand at the pole with the plaque START - you can safely ignore this.
Next lines contain words go X feet by azimuth Y - you are to extract numbers from them.
Last line contains phrase Dig here!
Answer should contain coordinates of the point where the Treasure is hidden, rounded to closest integers.

Example:

input data:
Stand at the pole with the plaque START
go 140 feet by azimuth 332
go 460 feet by azimuth 78
Dig here!

answer:
384 219
'''
import math
from sys import stdin

x = y = 0
for l in [line.rstrip() for i, line in enumerate(stdin) if i > 0]:
    if l == "Dig here!":
        print(round(x), round(y))
        break
    ft, az = [int(d) for d in l.split() if d.isdigit()]
    x = x + ft * math.sin(math.radians(az))
    y = y + ft * math.cos(math.radians(az))

