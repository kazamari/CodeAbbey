'''
Input data contains number of notes to identify.
The next line will provide the frequencies, separated by spaces.
Answer should contain identified note names.

Example:

input data:
16
185.4 115.3 203.9 55.2 52.7 86.6 932.3 229.8 61.8 66.1 363.7 771.4 594.4 48.2 102.6 222.4

answer:
F#3 A#2 G#3 A1 G#1 F2 A#5 A#3 B1 C2 F#4 G5 D5 G1 G#2 A3
'''
from math import log

notes = 'C C# D D# E F F# G G# A A# B'.split()


def from_hertz(hz):
    value = ((log((hz * 1024) / 440, 2) + 1 / 24) * 12 + 9)
    return ''.join([notes[int(value) % 12], str(int(value / 12) - 6)])


n = int(input())
print(*[from_hertz(x) for x in map(float, input().split())])