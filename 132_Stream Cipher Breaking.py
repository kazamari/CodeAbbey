# s = 'Hello, World!'
#
# s_ascii = [ord(x) for x in s]
# s_key = [(i * 51 + 13) % 256 for i in range(len(s))]
#
# s_hex = [format(x ^ y, 'x') for x, y in zip(s_ascii, s_key)]
#
# print('ASCII: ', *s_ascii)
# print('Key: ', *s_key)
# print('Result: ', *[x ^ y for x, y in zip(s_ascii, s_key)])
# print('Hex: ', *s_hex)
#
# print(*[int(x, 16) for x in s_hex])


# s1 = [int(x, 16) for x in 'b7.1d.6c.c8.19.a7.1a.11.4f.86.16.c2.af.77.5f.2e.20.72.ad'.split('.')]
# print(s1)

# def xor_encode(s, key):
#     s_ascii = [ord(x) for x in s]
#     # s_key = [(i * 51 + 13) % 256 for i in range(len(s))]
#     return '.'.join([format(x ^ y, 'x') for x, y in zip(s_ascii, key)])
#
# def xor_decode(s, key):
#     return [x ^ y for x, y in zip(s, key)]


s1 = 'b7.1d.6c.c8.19.a7.1a.11.4f.86.16.c2.af.77.5f.2e.20.72.ad'.split('.')
s2 = 'b6.10.71.91.4e.b5.1d.08.4c.ca.07.8d.ff.69.59.3a.29'.split('.')
s_xor = [int(x, 16) ^ int(y, 16) for x, y in zip(s1, s2)]

for i in range(len(s_xor)):
    a = s_xor[i] ^ int('20', 16)
    if ord('A') <= a <= ord('z'):
        print(i, chr(a))

        