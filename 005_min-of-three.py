'''
Input data will contain in the first line the number of triplets to follow.
Next lines will contain one triplet each.
Answer should contain selected minimums of triplets, separated by spaces.

Example:

data:
3
7 3 5
15 20 40
300 550 137

answer:
3 15 137

'''

n, list = int(input()), []
for i in range(n):
    x = map(int, input().split())
    list.append(min(x))

print(*list)
