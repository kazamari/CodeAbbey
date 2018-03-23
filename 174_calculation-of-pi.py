'''
Input data will contain value K between 100 and 200 which you will use to set radius as R = 10^K.
Another value N will be given - how many steps of algorithm to perform (so the last polygon has 6 * 2^N sides).
Answer should give the representation of Pi (without decimal point) after that many steps.

Example:

input data:
37 11

answer:
31415926193653839551895493120653182976

# 80 32
# 314159265358979323845486165352545943524907141145407199929352076303557146687045632

# 78 34
# 3141592653589793238462157025169875168637912936305417528874334282236256799686656
'''


def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


k, n = map(int, input().split())
R = D = 10**k

for i in range(n):
    d = D // 2
    D = isqrt(d**2 + (R - isqrt(R**2 - d**2))**2)

print(int(D * 6 * 2**n // 2))

