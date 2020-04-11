# Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive
# numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less
# than nine and relatively prime to nine, φ(9)=6.
# The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.
#
# Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.
#
# Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n)
# produces a minimum.
from UsefulFunctions import *
from decorators import *


spf = smallest_factors(10**7)
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

@timer
def main():
    min_total = 10
    for n in range(2, 10**7):
        p = phi(n)
        if sorted(str(n)) == sorted(str(p)) and min_total > n / p:
            print(n)
            min_total = n / p


if __name__ == '__main__':
    main()