import itertools

def gen_primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

primes = gen_primes()

print(list(itertools.islice(primes, 7-1, 7)))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
print(list(itertools.islice(primes, 1-1, 1)))
print(list(itertools.islice(primes, 199999-1, 199999)))
print(list(itertools.islice(primes, 4-1, 4)))