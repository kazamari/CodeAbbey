'''
You are given few thousands of IPs and you should return country codes for them. You will have only 1 minute to submit
the answer, so probably it is better to use binary search rather than iterate through the list.

Download our IP to Country list here

You may click it with the right mouse button and choose "Save As". Note that the file has unix-style line ends, so some
editors in windows could show it incorrectly, but you will anyway easily read separate lines programmatically.

The file has the slightly different format:

0 9zldr US
9zlds 73 AU
9zlkw lb CN

...

1q5gzcw 2db AU
1q5h1q8 8vn08v US

The integers of the first two columns are given in the numeral system with base 36 (just to make them shorter) - so
that for example in Python you may use something like this to convert them to ints:

s = '9zlkw'
n = int(s, 36)

The first integer in the line is the range-start itself. The second is the offset of range-end:

range_end = range_start + offset

For example in the second line offset is 73 which, converted to decimal, gives 255 - and you can check above that this
line really cares about IPs from 1.0.0.0 to 1.0.0.255.

Of course you may preprocess this file after downloading (for example, converting values to decimals if you like etc) -
but it is not necessary.

Input data will provide the amount of IPs to be processed in the first line.
Next lines will contain single IP each, also in base-36.
Answer should give country codes for these IPs, as two-letter tokens separated by spaces.
You have only about 1 minute to submit answer. Before processing input please reload the page so that new set of data
is generated and the timer is restarted.

Example:

input data:
10
1keei5f
bixots
1mmfpia
dwaviz
q0a5p9
l600w7
it4w75
ht85qa
1gvvigc
hg8y3f

answer:
AU BJ TW IN GB GE US CA EC PT
'''
from sys import stdin


def binarysearch(sequence, value):
    lo, hi = 0, len(sequence) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        range_start = int(sequence[mid].rstrip().split()[0], 36)
        range_end = range_start + int(sequence[mid].rstrip().split()[1], 36)

        if range_start <= value <= range_end:
            return sequence[mid].rstrip().split()[2]
        elif range_end < value:
            lo = mid + 1
        elif value < range_start:
            hi = mid - 1

    return None


with open('db-ip.txt', 'r') as f:
    sequence = f.readlines()
    print(*[binarysearch(sequence, int(line.rstrip(), 36)) for i, line in enumerate(stdin) if i > 0])
