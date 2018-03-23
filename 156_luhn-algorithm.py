'''
So please help Brother Kyprian to fix a list of bank card numbers. Some of them just miss one of digits and you should
restore this digit. Others have a pair of adjacent digits swapped - you are to find the leftmost pair which, if swapped,
makes valid card number.

All the card numbers would be 16 digits long (this is the most common length even in fairytales.

Input data contain a list of workers who have their card numbers incorrect.
Next lines contain a single card number each. If the number contains "?" (question mark) instead of some digit - this
digit should be restored. If all digits are present, then "swap-error" should be fixed.
Answer should contain a list of "fixed" card numbers.

Example:

input data:
4
?942682966937054
1217400151414995
2146133934?67114
2553514623364925

answer:
3942682966937054 1217040151414995 2146133934667114 2553514623369425
'''
from sys import stdin


def checksum(card_num):
    digits = list(map(int, card_num))
    return not ((sum(digits[-1::-2]) + sum([x * 2 if x * 2 < 10 else x * 2 - 9 for x in digits[-2::-2]])) % 10)


def restore_num(card_num):
    def swap(s, i, j):
        l_s = list(s)
        l_s[i], l_s[j] = l_s[j], l_s[i]
        return ''.join(l_s)

    if '?' in card_num:
        for i in range(10):
            if checksum(card_num.replace('?', str(i))):
                return card_num.replace('?', str(i))
    else:
        for i in range(len(card_num) - 1):
            test_num = swap(card_num, i, i+1)
            if checksum(test_num):
                return test_num


print(*[restore_num(line.rstrip()) for i, line in enumerate(stdin) if i > 0])


