'''
Input data will contain number of test-cases in the first line.
Following lines will contain a pair of numbers to compare each.
For Answer please enter the same amount of minimums separated by space, for example:

data:
3
5 3
2 8
100 15

answer:
3 2 15

'''

n, list = int(input()), []
for i in range(n):
    x, y = map(int, input().split())
    list.append(x if x < y else y)

print(*list)
