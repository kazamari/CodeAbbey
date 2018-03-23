'''
Input data contain M and N in the first line.
The second (rather long) line will contain M numbers separated by spaces.
Answer should contain exactly N values, separated by spaces. First should give amount of 1-s, second - amount of 2-s and so on.

Example:

data input:
10 3
3 2 1 2 3 1 1 1 1 3

answer:
5 2 3

'''

m, n = map(int, input().split())
count, l = [0 for _ in range(n)], map(int, input().split())

for i in l:
    count[i-1] += 1

print(*count)
