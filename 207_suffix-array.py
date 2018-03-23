'''
You are given some piece of text and your goal is to print out the suffix array for it. We do not discuss the algorithms
for building suffix arrays - they could be very fast and very complicated - but you can safely use naive approach for
the sample text will be just about 200 characters long. We want to learn the concept right now, not specific algorithm.

Input data will contain a single line of text (capital latin letters and spaces).
Answer should give a suffix array for this line - list of integers.

Example:

input data:
INTERPRETING CREATES RATES

answer:
12 20 22 16 13 15 3 24 18 7 11 9 0 10 1 5 21 14 6 4 25 19 2 23 17 8
'''


def suffix_array(str):
    return sorted(range(len(str)), key=lambda i: str[i:])


print(*suffix_array(input()))
