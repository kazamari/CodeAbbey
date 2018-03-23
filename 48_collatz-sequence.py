'''
Input data contains number of test-cases in the first line.
Second line contains the test-cases - i.e. the values for which calculations should be performed.
Answer should contain the same amount of results, each of them being the count of steps for getting Collatz Sequence to 1.

For example:

input data:
3
2 15 97

answer:
1 17 118

'''

def collatz_step(n):
    x, i = n, 0
    while x > 1:
        i += 1
        if x % 2 == 0:
            x /= 2
        else:
            x = 3 * x + 1
    return i

n = int(input())
print(*[collatz_step(x) for x in map(int, input().split())])
