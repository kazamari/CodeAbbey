'''
Our game will use words of 5 letters - any you will find in this list, including plurals like books and verbs in past
like bowed.

Input data contains a number N of word pairs to process.
Next N lines contain two words each.
Answer should contain minimum length of the path between words for each pair - i.e. the total count of words in the
chain, including starting and ending ones.

Example:

input data:
2
girls women
mayor clown

answer:
9 14

Here the following paths are possible:

women woken token tokes tikes tiles tills gills girls

mayor manor minor miner mines miles moles molts moots boots blots blows blown clown
'''
from sys import stdin


def ladder_len(start_word, end_word, dictionary):
    curr, next, explored = [start_word], [], set(start_word,)
    length = 1
    while curr:
        for word in curr:
            if word == end_word:
                return length
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + char + word[i + 1:]
                    if next_word not in explored and next_word in dictionary:
                        next.append(next_word)
                        explored.add(next_word)
        length += 1
        curr = next
        next = []
    return 0


with open('words.txt', 'r') as f:
    dictionary = set([line.rstrip() for line in f.readlines()])
    # print(ladder_len('mayor', 'clown', dictionary))
    print(*[ladder_len(*line.rstrip().split(), dictionary) for i, line in enumerate(stdin) if i > 0])
