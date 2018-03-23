'''
You are again to decrypt the encoded message but now instead of p and q you are given only their product n, just as a
real attacker. Encryption was still performed with e=65537, but unfortunately you have no idea of the decryption
exponent d!

However by chance you know that the person who encrypted the message was a perfect noob and used close values of p and
q, so you may find a way to factorize n easily enough.

Conversion between string and number is performed in the same way as in the RSA-related exercise mentioned above.

Input data will contain n in the first line.
The second line contains cipher which was generated as a^65537 mod n where a is the original text converted to long
integer.
Answer should contain the deciphered text.

Example:

input data:
2005386240811006492510206908835874977464399827995998174235015291258133373258958037573585627
258926557618335589879504876460462075566410747651590614428022205934562315249635550863811428

answer:
EGG EAT SKI SHY ARM EON HIP FUN LOW
'''


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


def isqrt(n):
  x = n
  y = (x + n // x) // 2
  while y < x:
    x = y
    y = (x + n // x) // 2
  return x


def fermat(n):
    a = isqrt(n)
    b2 = a * a - n
    b = isqrt(n)
    count = 0
    while b * b != b2:
        a = a + 1
        b2 = a * a - n
        b = isqrt(b2)
        count += 1
    p = a + b
    q = a - b
    assert n == p * q
    return p, q


def rsa_decrypt(n, c):
    e = 65537
    p, q = fermat(n)
    phi = n - p - q + 1
    d = modinv(e, phi)
    m = str(pow(c, d, n)).split('00')[0]
    return ''.join([chr(int(m[i:i + 2])) for i in range(0, len(m), 2)])


n = int(input())
cipher = int(input())

print(rsa_decrypt(n, cipher))