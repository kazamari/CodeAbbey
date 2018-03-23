'''
You should implement solution which works fast. A second or two is sufficient to run the proper solution (even with not
very modern computer).

Hint: you need not long arithmetic for this task.

Input data in the first line will contain the number of test-cases.
Next line will contain exactly this of divisors M for which you should give answers.
Answer should contain indices of members of Fibonacci Sequence, separated by spaces.

Example:

input data:
2
233328 433156

answer:
1620 282

Values will not exceed 2000000.
'''


def fib_div(m):
    a, b, i = 0, 1, 1
    while b % m != 0:
        a, b = b, (a + b) % m
        i += 1
    return i

n = int(input())
print(*[fib_div(x) for x in map(int, input().split())])
