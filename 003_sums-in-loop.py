'''
Input data will contain the total count of pairs to process in the first line.
The following lines will contain pairs themselves - one pair at each line.
Answer should contain the results separated by spaces.

Example:

data:
3
100 8
15 245
1945 54

answer:
108 260 1999

'''
n, list = int(input()), []
for i in range(n):
    x, y = map(int, input().split())
    list.append(x + y)

print(*list)
