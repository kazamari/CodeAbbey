'''
Now we are going to write a program to perform RSA decryption - it will give us necessary experience before trying to
hack this algorithm!

The text string is encoded as a long integer using the following approach:

    for each letter its two-digit decimal ASCII is written (so text will not use symbols with codes greater than 99);
    these two-digit values are simply concatenated;
    then 00 followed by several randomly choosen digits is added to the tail.

For example the word ABBA could be encoded as 6566666500314:

A    B    B    A  | end | few random digits
-----------------------------------
65   66   66   65 | 00  | 3   1   4

This integer is then encrypted by RSA and you should decrypt it back and print the original text string.

Adding some randomization is crucial for any public key cryptography system to prevent attacker guessing the original
message by trying to encrypt his guesses himself.

Input data will contain p and q at the first and second lines, while for e we choose popular constant value 65537.
The third line will contain the long integer value of cipher.
Answer should contain the decrypted text string.

Example:

input data:
30762542250301270692051460539586166927291732754961
29927402397991286489627837734179186385188296382227
424236952206057066872700453503661773567827006571091351397488406910437574827532103275742945321419387

answer:
TOWEL BEANS SWORD STOCK STORM CHECK
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


def rsa_decrypt(p, q, c):
    e = 65537
    n = p * q
    phi = n - p - q + 1
    d = modinv(e, phi)
    m = str(pow(c, d, n)).split('00')[0]
    return ''.join([chr(int(m[i:i + 2])) for i in range(0, len(m), 2)])


p = int(input())
q = int(input())
cipher = int(input())

print(rsa_decrypt(p, q, cipher))
