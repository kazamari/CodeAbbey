'''
You are given a sequence of notes - calculate frequencies for them using the explanations above.

Input data will have the number of notes in the first line.
Next line contains note names separated by spaces.
Answer should contain frequencies for these notes, rounded to nearest integer.

Example:

input data:
22
G#4 F#1 G#2 A#1 E5 A4 A#3 E1 A3 A2 D#5 G#5 B2 A1 F2 D5 F4 C#3 D1 B3 F#2 C#5

answer:
415 46 104 58 659 440 233 41 220 110 622 831 123 55 87 587 349 139 37 247 92 554
'''
notes = {n: i+1 for i, n in enumerate('C C# D D# E F F# G G# A A# B'.split())}


def to_hertz(nota):
    n, o = nota[:-1], int(nota[-1])
    return round(440/2**((4-o)+(10-notes[n])/12))


n = int(input())
print(*[to_hertz(x) for x in input().split()])
