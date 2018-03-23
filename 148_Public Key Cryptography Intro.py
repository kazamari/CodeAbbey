def modexp(a, b, m):
    ''' Modular Exponentiation '''
    r = 1
    while True:
        if b % 2 == 1:
            r = (r * a) % m
        b //= 2
        if b == 0:
            break
        a = (a * a) % m
    return r

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = egcd(b % a, a)
    return g, x - (b // a) * y, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x % m

def get_e(pe, p, n):
    for e in range(n):
        if modexp(p, e, n) == pe:
            return e
    return None


def decode(m):
    letters = [chr(i) for i in range(ord('a'),ord('z')+1)]
    return ''.join([letters[(m // (31 ** i)) % 31] for i in range(4)][::-1])

n, p, pe = 10001331, 372453, 464079
pk, c = 615510, 932705

print(get_e(pe, p, n))

# alphabeth = [chr(i) for i in range(ord('a'),ord('z')+1)]
# print(alphabeth)
#
# word = 'math'
#
# int_word = sum([alphabeth.index(x)*(31**(len(word) - 1 - i)) for i, x in enumerate(word)])
# print(int_word)
#
# print(decode(int_word))
#
#

# print([alphabeth[(358088 // (31 ** i)) % 31] for i in range(4)][::-1])
