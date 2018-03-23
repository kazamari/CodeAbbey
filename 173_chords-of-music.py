'''
You are given several notes described by their numbers according to MIDI-standard - C of the 0-th octave is 0, D in the
same octave is 2, B is 11 and so on, so that 64 means E of the 5-th octave.

The task is to determine what chord these notes represent.

Input data contain the number of test-cases in the first line.
Next lines contain from 3 or more integers - numbers of notes played.
Answer should contain respective chord names in form C-minor, F#-major or the word other in cases when notes do not form
one of these two chords at all.

Example:

input data:
3
87 73 64 61
46 37 53 58 70
44 48 51 56 32

answer:
other A#-minor G#-major
'''
from sys import stdin

notes = 'C C# D D# E F F# G G# A A# B'.split()


def is_chord(chord):
    chord = sorted({notes[x % 12] for x in map(int, chord.split())}, key=lambda x: notes.index(x))
    for root in chord:
        if notes[(notes.index(root) + 7) % 12] in chord:
            if notes[(notes.index(root) + 3) % 12] in chord:
                return root+'-minor'
            elif notes[(notes.index(root) + 4) % 12] in chord:
                return root+'-major'
    else:
        return 'other'


print(*[is_chord(line.rstrip()) for i, line in enumerate(stdin) if i > 0])
