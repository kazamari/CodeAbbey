import math
for i in range(3):
    slope=map(int, input().split())
    cpts=[]
    for num,p in enumerate(slope[1:]):
        if p != slope[num]: cpts.append(((num+1)*4,p*4))
    for j in range(3):
        v,angle=map(float, input().split())
        vx,vy=v*math.cos(angle*math.pi/180.0),v*math.sin(angle*math.pi/180.0)
        for n,pt in enumerate(cpts):
            t=float(pt[0])/vx
            y=vy*t-9.81*t**2/2.0
            if y > pt[1]: continue
            if y >= cpts[n-1][1]:
                print(int(math.floor(pt[0])))
            else:
                height = cpts[n-1][1]
                D=math.sqrt(vy*vy-2*9.81*height)
                t=(D+vy)/9.81
                print(int(math.floor(vx*t)))
            break


g = 9.81
slope = list(map(int, '0 0 0 0 0 1 1 1 1 2 2 2 2 2 2 3 4 5 6 6 7 8 9 9 10 10 10 10 10 10 11 11 12 13 14 15 16 16 17 18'.split()))
V, A = map(int, '42 42'.split())

# cpts = []
# for num, p in enumerate(slope[1:]):
#     if p != slope[num]:
#         cpts.append(((num + 1) * 4, p * 4))
#
# print(cpts)

vx, vy = V * math.cos(math.radians(A)), V * math.sin(math.radians(A))