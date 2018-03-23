# l=int(input())
# for i in range(l):
#     pA, pB = [float(x)/100.0 for x in input().split()]
#     pAwin, pBwin = 0, 0
#     for t in range(0, 10000)[::-1]:
#         prob = (1.0 - pA)**(t / 2) * (1.0 - pB)**(t - t / 2)
#         pAwin, pBwin = pAwin + pA * prob * ((t + 1) % 2), pBwin + pB * prob * (t % 2)
#     print(int(round(pAwin * 100)))


pA, pB = map(int, '30 50'.split())
