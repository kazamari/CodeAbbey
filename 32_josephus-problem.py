'''
Your task is to determine for given number of people N and constant step K the position of a person who remains
the last - i.e. the safe position. For example if there are 10 people and they eliminate each third:

N = 10, K = 3

sequence of counting looks like this (brackets show persons who are elimintated):

1st round: 1 2 (3) 4 5 (6) 7 8 (9) 10
2nd round:                            1 (2) 4 5 (7) 8 10
3rd round:                                                (1) 4 5 (8) 10
4th round:                                                               4 (5) 10
5th round:                                                                        4 (10)

so the "winner" is one who was #4 at initial standing.

Input data will contain number of people N and the counting step K.
Answer should contain the number of person who will remain at the end. Initial numbering starts from 1.

Example:

initial data:
10 3

answer:
4
'''


def joseph(n, k):
    if n == 1:
        return 1
    else:
        return (joseph(n - 1, k) + k - 1) % n + 1


n, k = map(int, input().split())
print(joseph(n, k))
