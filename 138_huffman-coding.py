'''
Given a fragment of text you will be asked to find the compression ratio provided by Huffman's algorithm:

             original size
ratio = -----------------------
            compressed size

I.e. in case with DAVIDAHUFFMAN original size is 13*8=104 bits while compressed size is only 40 bits, so the compression
ratio is 2.6. We assume that original text was encoded using 8 bits per character.

*With real

Input data will contain a sample of text, consisting of letters, punctuation marks, spaces and probably digits.
Answer should contain a single real value - the compression ratio (with 1e-6 precision or better).

Example:

input data:
DAVIDAHUFFMAN

answer:
2.6

Note that real implementation of the algorithm also needs to store the code-table or counts-table in the resulting
file - this slightly reduces the compression ratio especially if the original size is comparatively small.
'''
from heapq import heappush, heappop, heapify


def encoded_table(s):
    # fr_table = sorted({x: s.count(x) for x in s}.items(), key=lambda x: x[1], reverse=True)
    fr_table = {x: s.count(x) for x in s}
    heap = [[w, [symb, '']] for symb, w in fr_table.items()]
    heapify(heap)
    while len(heap) > 1:
        right = heappop(heap)
        left = heappop(heap)
        for pair in right[1:]:
            pair[1] = '0' + pair[1]
        for pair in left[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [right[0] + left[0]] + right[1:] + left[1:])
    return [[s, fr_table[s], b] for s, b in sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))]


s = input()
original_size = len(s) * 8
comressed_size = sum([b * len(c) for a, b, c in encoded_table(s)])

print(original_size / comressed_size)
