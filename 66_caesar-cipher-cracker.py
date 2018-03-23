'''
Input data will contain the number of encrypted messages in the first line.
Next lines will contain the encrypted lines themselves. Each line is encoded with separate key!
Answer should contain three first words of each decrypted line followed by the value of the key. Several answers should
be separated with spaces.

Additional info:

    the key will always be a value between 1 and 25 inclusive;
    lines will contain only capital latin letters and spaces to separate words;
    original messages are in English, from 60 to 100 characters long.

Example:

input data:
2
XIP DBSFT PG ESFBNT
VJQWIJ KV OCMGU VJKPIU XGTA SWGGT

answer:
WHO CARES OF 1 THOUGH IT MAKES 2
'''
import sys

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
frequency = [8.1, 1.5, 2.8, 4.3, 13.0, 2.2, 2.0, 6.1, 7.0, 0.15, 0.77, 7.0, 2.4,
             6.8, 7.5, 1.9, 0.095, 6.0, 6.3, 9.1, 2.8, 0.98, 2.4, 0.15, 2.0, 0.074]


def cipher(s, k):
    return ''.join([alphabet[(alphabet.index(c) + k) % len(alphabet)] if c in alphabet else c for c in s.upper()])


def get_frequency(s):
    n = sum(1 for c in s.upper() if c in alphabet)
    return [100.0 * (float(s.count(x)) / n) for x in alphabet]


def rotate(xs, n):
    return xs[n:] + xs[:n]


def sqr(xs, ys):
    return sum((x - y) ** 2 for x, y in zip(xs, ys))


def crack(s):
    table = get_frequency(s)
    chi_tab = [sqr(rotate(table, n), frequency) for n in range(len(alphabet))]
    shift = chi_tab.index(min(chi_tab))
    return [cipher(s, -shift), shift]


for line in sys.stdin:
    s, k = crack(line.rstrip())
    print(' '.join(s.split()[:3]), k, end=" ")
