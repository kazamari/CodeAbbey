'''
Input data contains N+1 values, first of them is N itself (Note that you should not try to convert it).
Answer should contain exactly N results, rounded to nearest integer and separated by spaces.

Example:

data:
5 495 353 168 -39 22
answer:
257 178 76 -39 -6

Please note that first 5 is not a temperature, but the amount of values to convert!
'''

def round_to_int(n):
    return int(n+0.5) if n-int(n) == 0.5 else round(n)

far = list(map(int, input().split()))
print(*[round_to_int((x - 32) * 5 / 9) for x in far[1:]])
