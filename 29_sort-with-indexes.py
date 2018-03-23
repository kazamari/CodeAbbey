'''
Initial data will contain array size at first line and array values itself in the second (integers separated by spaces).
Answer should contain initial indexes of the array members after they are reordered by sorting.

Example:

input data:
4
50 98 17 79

answer:
3 1 4 2

'''

n = int(input())
list = list(map(int, input().split()))

print(*[x + 1 for x in sorted(range(n), key=lambda i: list[i])])
