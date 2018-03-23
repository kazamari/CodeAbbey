m, n = 4, 10
points = [[0, 180], [90, 0], [180, 120], [270, 60]]

def findpt(points, n):
    newpts=[]
    for i in range(n):
        alpha = i / (1 - n - i)
        for i in range(1, len(points)):
            dx = points[i][0] - points[i-1][0]
            dy = points[i][1] - points[i-1][1]
            newx = points[i-1][0] + dx * alpha
            newy = points[i-1][0] + dy * alpha
            newpts.append([newx, newy])

    return newpts


print(findpt(points, n))



# l,dalph = map(int, raw_input().split())
# pts=[]
# for i in xrange(l):
#     a,b = map(int, raw_input().split())
#     pts.append({'x':a,'y':b})
# for i in xrange(dalph):
#     pt = findpt(pts, float(i)/(dalph-1))
#     print int(round(pt['x'])),int(round(pt['y'])),