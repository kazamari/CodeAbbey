
def getmax(maxv, isles):
    n = len(isles)-1
    while n >= 0:
        np2 = maxv[n+3] if n+3 < len(isles) else 0
        np1 = maxv[n+2] if n+2 < len(isles) else 0
        print(np2, np1)
        maxv[n] = max(np2, np1) + isles[n]
        print(maxv)
        n -= 1
    return maxv[0]


isles=list(map(int, '11 5 3 17 2 13 19 7'.split()))
maxv=[0]*len(isles)
maxv[-1] = isles[-1]
print(maxv)
print(getmax(maxv, isles))

# isles=list(map(int, '11 5 3 17 2 13 19 7'.split()))
# candies = []
#
# n = 0
# candies.append(isles[n])
# candies.append(isles[-1])
# while n < len(isles)-2:
#     if isles[n+2] >= isles[n+3]:
#         candies.append(isles[n+2])
#         n = n + 2
#     else:
#         candies.append(isles[n + 3])
#         n = n + 3
#
# print(candies)
