import itertools

# def gen_primes():
#     D = {}
#     q = 2
#     while True:
#         if q not in D:
#             yield q
#             D[q * q] = [q]
#         else:
#             for p in D[q]:
#                 D.setdefault(p + q, []).append(p)
#             del D[q]
#         q += 1

# print(list(itertools.takewhile(lambda x : x <= 31, gen_primes())))
# # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

from sys import stdin

def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

def is_emirp(n):
    if not is_prime(n):
        return False
    rev = 0
    while n != 0:
        d = n % 10
        rev = rev * 10 + d
        n = int(n / 10)
    return is_prime(rev)

def prime_emirp(num):
    i = num
    while True:
        if is_emirp(i):
            return(i)
        i += 1

# print(*[prime_emirp(int(line.rstrip())) for i, line in enumerate(stdin) if i > 0])

print(prime_emirp(90359729279070953671905))

#
# # Python3 code to check if
# # given number is Emirp or not.
#
# # Returns true if n is prime.
# # Else false.
# def isPrime(n):
#     # Corner case
#     if n <= 1:
#         return False
#
#     # Check from 2 to n-1
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#
#     return True
#
#
# # Function will check whether
# # number is Emirp or not
# def isEmirp(n):
#     # Check if n is prime
#     n = int(n)
#     if isPrime(n) == False:
#         return False
#
#         # Find reverse of n
#     rev = 0
#     while n != 0:
#         d = n % 10
#         rev = rev * 10 + d
#         n = int(n / 10)
#
#     # If both Original and Reverse
#     # are Prime, then it is an
#     # Emirp number
#     return isPrime(rev)
#
#
# # Driver Function
# n = 13  # Input number
# if isEmirp(n):
#     print("Yes")
# else:
#     print("No")
#
# # This code is contributed by "Sharad_Bhardwaj".