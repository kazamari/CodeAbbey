def distance(s):
    dst = lambda x1, y1, x2, y2: ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    x1, y1, x2, y2, xp, yp = map(int, s.split())

    a, b, c = y1 - y2, x2 - x1, x1 * y2 - x2 * y1

    dp = abs(a * xp + b * yp + c) / (a**2 + b**2)**0.5

    d1, d2, dl = dst(x1, y1, xp, yp), dst(x2, y2, xp, yp), dst(x1, y1, x2, y2)

    truedst = dp
    if d1**2 - dp**2 > dl**2: truedst = d2
    if d2**2 - dp**2 > dl**2: truedst = d1

    return truedst