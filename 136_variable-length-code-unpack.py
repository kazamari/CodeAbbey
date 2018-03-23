'''
Hope you've already solved Variable Length Code problem and have written a program to compress the text. Now our goal
is to decompress it back.

Use the same code-table to decrypt the result of compression of some message. The most effective way is to represent
the table as a binary tree with letters in the leaves and use bits of the stream to traverse this tree from the root.

To make the exercise look bit more different we use another way of representing compressed stream. It is split into
chunks of 5 bits (instead of 8) and then these chunks are converted to digits of numeral system with base 32, i.e.
one of the characters:

0123456789ABCDEFGHIJKLMNOPQRSTUV

For example the compressed sequence:

0SA14NH2CG2K8GH1GOD604

represents the following bit stream:

00000 11100 01010 00001 00100 10111 10001 00010 01100 10000 00010 10100 01000 10000 10001 00001
10000 11000 01101 00110 00000 00100

And at the end it is just encoding of the same phrase world of !programming (which we have seen already).

Note that the compressed stream could be padded with trailing zeroes, which anyway do not correspond to any character
in the table and so could be unambiguously removed.

Input data contain a single string - very long 32-based number, representing the compressed data.
Answer should contain the decoded text.

Example:

input data:
44TGUUM8OAIBI4Q01JI0M462KALCA0

answer:
!i am a stupid !text !compressor
'''
abc = {b: format(a, 'b').zfill(5) for (a,b) in enumerate('0123456789ABCDEFGHIJKLMNOPQRSTUV')}
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


def unpack(s):
    encoded_s, res, is_find = ''.join([abc[x] for x in s]), [], True
    while is_find:
        for key, value in codes.items():
            if encoded_s.find(value) == 0:
                encoded_s = encoded_s[len(value):]
                res.append(key)
                break
        else:
            is_find = False
    return ''.join(res)


print(unpack(input()))