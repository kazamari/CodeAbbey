'''
Input data will give you exactly 300 numbers in a single line.
Answer should contain maximum and minimum of these values, separated by space.

Example:

input data:
1 3 5 7 9 11 ... 295 297 299 300 298 296 ... 12 10 8 6 4 2

answer:
300 1

'''

array = list(map(int, input().split()))

min = max = array[0]

for x in array[1:]:
    if x > max:
        max = x
    if x < min:
        min = x

print(max, min)
