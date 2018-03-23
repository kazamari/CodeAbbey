import math
from decimal import Decimal

def get_fib_index(n):
    # phi = (1 + math.sqrt(5)) / 2
    # return round(math.log(n * math.sqrt(5) + 0.5, phi))
    return math.log(n * math.sqrt(5) + 0.5) / math.log(1.61803398875) - 1

print(get_fib_index(99194853094755497))

