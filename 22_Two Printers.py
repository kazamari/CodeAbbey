import math

def printing_time(x, y, n):
    a = math.ceil((y * n) // (x + y))
    b = math.ceil((x * n) // (x + y))


    return min(times)

print(printing_time(3, 5, 4))