'''
Input data has the following format:

    first line contains N - amount of values to sum;
    second line contains N values themselves.

Answer should contain a single value - the sum of N values.

Example:
input data:
8
10 20 30 40 5 6 7 8

answer:
126
'''
n = int(input())
list = map(int, input().split())
print(sum(list))
