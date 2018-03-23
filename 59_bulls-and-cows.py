'''
Your goal is to write a program which calculates the values which should be told as a hint to the given guess.

Input data will contain the secret value and the number of guesses in the first line.
Second line will contain the specified amount of guesses.
Answer should contain hints for these guesses, they should be given in format X-Y and separated with spaces.

Example:

input data:
1492 5
2013 1865 1234 4321 7491

answer:
0-2 1-0 1-2 0-3 2-1
'''

num, num_of_guesses = input().split()
lst = input().split()

for x in lst:
    b, c = 0, 0
    for i in range(4):
        if x[i] == num[i]:
            b += 1
        elif x[i] in num:
            c += 1
    print('{}-{}'.format(b, c), end=" ")
