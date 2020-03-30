# Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine
# the number of numbers less than n which are relatively prime to n.
# For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
#
# n	Relatively Prime	φ(n)	n/φ(n)
# 2	1	1	2
# 3	1,2	2	1.5
# 4	1,3	2	2
# 5	1,2,3,4	4	1.25
# 6	1,5	2	3
# 7	1,2,3,4,5,6	6	1.1666...
# 8	1,3,5,7	4	2
# 9	1,2,4,5,7,8	6	1.5
# 10	1,3,7,9	4	2.5
# It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.
#
# Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
from UsefulFunctions import *
import numpy
from decorators import *


def bruteForce():
    max = 0
    for i in range(2, 100000001):
        phi = i - 1
        for j in range(phi, 1, -1):
            if gcd(i, j) > 1:
                phi -= 1
        result = i / phi
        max = i if result > max else max
    print(max)


# def smallest_factors(n):
#     # set each number to itself
#     spf = [i for i in range(n)]
#
#     # starting at 2, see if the number is prime/hasn't been changed
#     # then mark every number that is divisible by that number
#     # this method gets the smallest prime factor of a number.
#     for i in range(2, len(spf)):
#         if i == spf[i]:
#             for j in range(i * i, len(spf), i):
#                 if spf[j] == j:
#                     spf[j] = i
#     return spf


spf = smallest_factors(1000001)
print(spf)


# The general formula to compute φ(n) is the following:
# If the prime factorisation of n is given by n =p1^e1*...*pn^en, then φ(n) = n *(1 - 1/p1)* ... (1 - 1/pn).
def phi(n):
    if spf[n] == n:
        return n - 1
    factors = []
    nt = n
    while nt != 1:
        factors += [spf[int(nt)]]
        nt //= spf[nt]
    factors = list(dict.fromkeys(factors))
    # print(factors)
    for factor in factors:
        n *= (1 - (1 / factor))
    return int(n + .5)


def v1():
    vals = [n / phi(n) for n in range(2, 100000001)]
    return vals.index(max(vals)) + 2


def v2():
    maximum_result = 0
    maximum_n = 0
    for n in range(2, 1000001):
        result = n / phi(n)
        if result > maximum_result:
            maximum_result = result
            maximum_n = n
    return maximum_n

@timer
def main():
    print(phi(2))
    print(phi(3))
    print(phi(4))
    print(phi(5))
    print(phi(6))
    print(phi(7))
    print(phi(8))
    print(phi(9))
    print(phi(10))
    print(v2())


if __name__ == '__main__':
    main()
