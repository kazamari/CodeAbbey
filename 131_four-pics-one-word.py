'''
Input data contain the number of testcases in the first line.
Each of the following lines contains the required length of the word and a set of letters.
Answer should contain the amount of words from dictionary satisfying each case.

Example:

input data:
2
3 t c a z
3 t c a f

answer:
2 4

First case allows words cat and act while second adds fat and aft to them.
'''
from sys import stdin


def amount_words(dictionary, s):
    n, letters = s.split(' ', 1)
    n, letters, counter = int(n), letters.split(), 0
    for word in dictionary:
        if len(word.rstrip()) == n:
            word = word.rstrip()
            for char in word:
                if word.count(char) > letters.count(char):
                    break
            else:
                counter += 1
    return counter


with open('words.txt', 'r') as f:
    dictionary = f.readlines()
    print(*[amount_words(dictionary, line.rstrip()) for i, line in enumerate(stdin) if i > 0])

