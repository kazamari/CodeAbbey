'''
You need to write encoder and decoder for Base32. Please follow the specifications below.

Source message should be at first "padded" with one or more symbols so that its total length is a multiple of 5. These
symbols should be just integer values showing how many symbols were added. I.e.:

Hi          ->  Hi333
Bye         ->  Bye22
John        ->  John1
Abbey       ->  Abbey55555
Jeopardy    ->  Jeopardy22
CodeMasters ->  CodeMasters4444

With such padding we later will need only to peek at the last symbol to understand by which amount the string should be
reduced.

Then take every 5-bytes chunk of the source message and write it down as bits (converting symbols to their ASCII values
and then to binary octets). So that John1 becomes:

John1 => 74 111 104 110 49 =>

01001010  01101111  01101000  01101110  00110001

Now this binary line is just glued together and split into chunks of 5:

01001  01001  10111  10110  10000  11011  10001  10001 =>

  9      9     23     22     16     27     17     17

And with alphabet shown above it will be encoded as JJXWQ3RR.

We hope that you will be able to work out how to proceed with decoding on your own.

Input data will give total amount of test-cases in the first line.
Next lines will contain one test-case each, of them odd lines (1-st, 3-rd, 5-th) will contain normal text to be encoded
while remaining will contain Base32 data to decode.
Answer should contain encoded and decoded phrases, all glued with spaces (it is not a problem that some phrases contain
spaces themselves).

Example:

input data:
6
Ng Sir three
ONUXIIDUNBZGKZJAMR2WK3DMNFXGOIDTNF2CAZDVMVWGY2LOM42DINBU
Sir
ONUXIIDUNBZGKZJAONUXIMRS
blind Ng
MJWGS3TEGU2TKNJV

answer:
JZTSAU3JOIQHI2DSMVSTGMZT sit three duelling sit duelling KNUXEMRS sit three sit MJWGS3TEEBHGOMRS blind

Note: please, try to avoid the idea of creating real binary string and splitting it with string functions. This will
work, but it would not be "production-ready" solution since it would be slow. Instead try to deal with numbers
(integers) directly.
'''
import sys

_b32tab2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567'


def b32encode(s):
    leftover = len(s) % 5
    s = s + str(5 - leftover) * (5 - leftover)
    binary_string = ''.join(["{0:08b}".format(ord(x)) for x in s])
    return ''.join([_b32tab2[int(binary_string[i:i + 5], 2)] for i in range(0, len(binary_string), 5)])


def b32decode(s):
    binary_string = ''.join(["{0:05b}".format(_b32tab2.index(x)) for x in s])
    res = [chr(int(binary_string[i:i + 8], 2)) for i in range(0, len(binary_string), 8)]
    return ''.join(res[:-int(res[-1])])


print(*[b32encode(line.rstrip()) if i % 2 != 0 else b32decode(line.rstrip())for i, line in enumerate(sys.stdin) if i > 0])
