'''
You will be given several cards represented by their values (from 0 to 51). You will need to print out their names.

Input data will contain the amount of cards in the first line.
Next line will contain the card values themselves.
Answer should contains card names in form Rank-of-Suit, e.g. Queen-of-Spades, 2-of-Clubs separated with spaces. Use the
names as given above.

Example:

input data:
5
25 32 51 20 6

answer:
Ace-of-Spades 8-of-Diamonds Ace-of-Hearts 9-of-Spades 8-of-Clubs
'''

suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']


def card(card_value):
    suit = suits[card_value // 13]
    rank = ranks[card_value % 13]
    return '{}-of-{}'.format(rank, suit)


n = int(input())
print(*[card(x) for x in map(int, input().split())])
