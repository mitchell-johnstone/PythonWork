def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)


# Python program to print prime factors

import math


# A function to print all prime factors of
# a given number n
def primeFactors(n):
    # Print the number of two's that divide n
    while n % 2 == 0:
        print(2)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            print(i)
            n = n / i

            # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print(n)

import numpy


def smallest_factors(n):
    # set each number to itself
    spf = numpy.zeros(n, dtype=int)

    # starting at 2, see if the number is prime/hasn't been changed
    # then mark every number that is divisible by that number
    # this method gets the smallest prime factor of a number.
    for i in range(2, n):
        if not spf[i]:
            spf[i] = i
            for j in range(i * i, n, i):
                if not spf[j]:
                    spf[j] = i
    return spf
