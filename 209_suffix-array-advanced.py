'''
So let us try building suffix array over the larger text. Good books, like The Holy Bible or Lord of the Rings contains
usually few hundreds thousand words, so let us create similar data set.

    We will load words from our favorite words.txt file into single list.
    Then we set up Linear Congruential Generator with the usual parameters (A = 445, C = 700001, M = 2097152).
    And we'll generate N random values starting with given seed - then turning these values into indices for the word
    list (taking modulo by the size of the list if necessary).
    Let us concatenate these extracted words with spaces into a single string (thus representing a large book), and
    then build suffix array for such a string.
    To check the answer we'll use array checksum - just as in that old problem.

Input data will contain two integers - amount of words N to create a "book", and the initial value X0 for our random
generator.
Answer should contain checksum of the resultant suffix array.

Time limit - 90 seconds - please do not forget to reload the page to generate new data and reset timer before copying
these data to your program.

Example:

input data:
9 13

answer:
7897656

Explanation:

With seed of 13 we generate 9 random values:

705786 201971 399560 246281 1243142 250063 828980 497349 1819346

Corresponding to words from list with the following indices:

1808 9977 15572 54287 27180 58069 61004 49363 27402

e.g. forming the following string:

anagrams clumsy dingy storks hurt townspeople vaguest scrimshawing icicle

and then the suffix array is calculated as following:

[73, 8, 15, 28, 66, 53, 21, 33, 45, 2, 47, 5, 0, 61, 68, 70, 9, 55, 16, 72, 44, 40, 50,
    65, 3, 48, 19, 60, 29, 67, 69, 57, 63, 17, 26, 71, 43, 10, 6, 58, 12, 1, 64, 18, 37,
    41, 24, 35, 39, 42, 4, 56, 25, 31, 7, 27, 54, 59, 38, 51, 22, 13, 52, 32, 23, 34, 49,
    11, 30, 46, 62, 36, 14, 20]

Note that the empty string is also included into suffix array and takes the very first place (for string S of the
length L it is substring(S, start = L, length = 0)).
'''
from collections import defaultdict


def sort_bucket(str, bucket, order):
    d, res = defaultdict(list), []
    for i in bucket:
        d[str[i:i + order]].append(i)
    for k, v in sorted(d.items()):
        if len(v) > 1:
            res += sort_bucket(str, v, order * 2)
        else:
            res.append(v[0])
    return res


def suffix_array(str):
    return sort_bucket(str, (i for i in range(len(str)+1)), 1)


def check_sum(list):
    sum = 0
    for x in list:
        sum = (sum + x) * 113
        if sum > 10000007:
            sum %= 10000007
    return sum


def lcg(a, c, modulus, seed):
    while True:
        seed = (a * seed + c) % modulus
        yield seed


def get_words(seed, n):
    generator = lcg(445, 700001, 2097152, seed)
    with open('words.txt', 'r') as f:
        words = [line.rstrip() for line in f]
        q = len(words)
    return ' '.join([words[next(generator) % q] for _ in range(n)])


n, seed = map(int, input().split())

print(check_sum(suffix_array(get_words(seed, n))))