'''
Use algorithm from the task Funny Words Generator to create a list of exactly 900000 words, each 6 letters long.
You should use exactly the same Linear Congruential Generator as random generator. The only input parameter would be
the seed for your random number generator (LCG).

Input data will contain a single value - the seed for random generator which you will use to generate list of words.
Answer should contain a single word - one most frequently encountered in the list.

Example:

input data:
99658

answer:
riguzi

Test-cases are selected so that there would be only one most frequent word for each given seed.
'''


def lcg(a, c, modulus, seed):
    while True:
        seed = (a * seed + c) % modulus
        yield seed


def word(gnr):
    consonants, vowels = 'bcdfghjklmnprstvwxz', 'aeiou'
    return ''.join((consonants[z % 19] if i % 2 == 0 else vowels[z % 5] for i, z in enumerate(gnr)))


def words_generator(seed, n):
    generator = lcg(445, 700001, 2097152, seed)
    for i in range(n):
        yield word((next(generator) for _ in range(6)))


def fr(words):
    dict = {}
    for word in words:
        if word in dict.keys():
            dict[word] += 1
        else:
            dict.update({word: 1})
    return sorted(dict.items(), key=lambda x: x[1], reverse=True)[0][0]


n, seed = 900000, int(input())
print(fr(words_generator(seed, n)))
