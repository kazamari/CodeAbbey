'''
Let us encode the string world of !programming (you see, P is written as !p here).

Working with the table above we construct the following sequence:

w       o     r     l      d        o     f         !      p       r     o     g       r
0000011 10001 01000 001001 00101 11 10001 000100 11 001000 0000101 01000 10001 0000100 01000

a   m      m      i     n     g
011 000011 000011 01001 10000 0000100

Now let us join these bits into a single sequence and then split it into chunks of 8 bits - one chunk for one byte
(adding few 0 at the end if the last byte has less than 8 bits):

00000111 00010100 00010010 01011110 00100010 01100100 00000101 01000100 01000010 00100001 10000110
00011010 01100000 00010000

It is more convenient to print bytes in hexadecimal, so result could be written as:

07 14 12 5E 22 64 05 44 42 21 86 1A 60 10

Note that while initial sequence consisted of 21 characters the result have only 14 bytes (more exactly 13.875 since
we added one padding zero). So if we store this text in ASCII we spend 7 more bytes or 50%. Of course it is also due
to the fact that we created encoding just for letters and not for all possible bytes.

If we use some 5-bit telegraph encoding (sufficient for 26 letters and 6 more symbols) we'll need only 13.125 bytes,
i.e. even less than we used - this is because our test phrase have very "uncommon" letters distribution (many o-s and
not a single e for example). ITA2 will require 14.375 bits (check it!)

Input data contains a line of text consisting only of characters from the table above.
Answer should contain byte sequence produced by our encoding algorithm using this table (in hexadecimal).

Example:

input data:
entertaining interpreter

answer:
B0 9A 89 69 82 60 13 4C 26 A0 2A 2C D4 00
'''
codes = {
    ' ': '11',             'e': '101',
    't': '1001',           'o': '10001',
    'n': '10000',          'a': '011',
    's': '0101',           'i': '01001',
    'r': '01000',          'h': '0011',
    'd': '00101',          'l': '001001',
    '!': '001000',         'u': '00011',
    'c': '000101',         'f': '000100',
    'm': '000011',         'p': '0000101',
    'g': '0000100',        'w': '0000011',
    'b': '0000010',        'y': '0000001',
    'v': '00000001',       'j': '000000001',
    'k': '0000000001',     'x': '00000000001',
    'q': '000000000001',   'z': '000000000000'
}


def encode(s):
    bits = ''.join([codes[l] for l in s])
    return [format(int(bits[i:i+8].ljust(8, '0'), 2), '02X') for i in range(0, len(bits), 8)]


print(*encode(input()))
