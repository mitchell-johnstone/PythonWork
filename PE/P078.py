# Let p(n) represent the number of different ways
# in which n coins can be separated into piles.
# For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.
# OOOOO
# OOOOc2a0 c2a0O
# OOOc2a0 c2a0OO
# OOOc2a0 c2a0Oc2a0 c2a0O
# OOc2a0 c2a0OOc2a0 c2a0O
# OOc2a0 c2a0Oc2a0 c2a0Oc2a0 c2a0O
# Oc2a0 c2a0Oc2a0 c2a0Oc2a0 c2a0Oc2a0 c2a0O
# Find the least value of n for which p(n) is divisible by one million.
from decorators import *
import numpy as np
import math


Pn = [1, 1]
def calcP(n):
    global Pn
    n = int(n)
    if n < 0: return 0
    while len(Pn) <= n:
        Pn += [0]
    if Pn[n] > 0: return Pn[n]
    P = 0
    for k in range(1,n): #int(n**.5)):
        n1 = n - k*(3*k-1)/2
        n2 = n - k*(3*k+1)/2
        Pn1 = calcP(n1)
        Pn2 = calcP(n2)
        if k%2 ==1: P += (Pn1 + Pn2)
        else: P-=(Pn1+Pn2)
    Pn[n] = P
    return P


def v1():
    i = 0
    s = 0
    while not s or s%1000000!=0:
        i += 1
        print(i)
        s += calcP(i)
    print(s)
    print(i)


primes = []
def generatePrimeList():
    global primes
    f = open("AllPrimes.txt")
    for line in f.readlines():
        # print(line)
        primes += [int(i) for i in line.split(" ") if i and i != "\n"]
    #print(primes)
    f.close()


# function to sum the divisors of n
# note: does not have to be prime divisors, but rather all divisors of n.
# for each prime p, with multiplicity k, we have:
# S(pk) = 1 + p + p2 + . . . + pk = (pk+1 - 1) / (p-1) .
# and then S(n) = sum(S(p1**k1),S(p2**k2),...)
sodn = []
def sod(n):
    global primes, sodn
    if n <= 0: return 0
    while len(sodn) <= n: sodn+=[0]
    if sodn[n] > 0: return sodn[n]
    result = 1
    cn = n
    for p in primes:
        k=0
        while cn%p==0:
            cn//=p
            k+=1
        if k:
            result *= (p**(k+1)-1)//(p-1)
        if cn == 1: break
    sodn[n] = result
    return result


def calcP2(n):
    global Pn
    if n < 0: return 0
    if n == 0: return 1
    while len(Pn) <= n:
        Pn += [0]
    if Pn[n] != 0: return Pn[n]
    for k in range(n):
        Pn[n] += ((sod(n-k)%10**6) * (calcP2(k)%10**6)) % 10**6
    Pn[n] //= n%10**6
    # Pn[n] = (sum([(sod(n-k)*calcP2(k)) for k in range(n)])//n)
    return Pn[n]


def v2():
    generatePrimeList()
    s=0
    i = 0
    while calcP2(i)%1000000!=0:
        #print(i, ": ", calcP2(i))
        print(i)
        i+=1
    print(i)


def calcP3(n):
    global Pn
    if n < 0: return 0
    while len(Pn)<=n: Pn += [0]
    if Pn[n]: return Pn[n]
    # cap = int(((24*n+1)**.5-1)//6)
    for k in range(1,n//2+1):
        t1 = n-k*(3*k-1)//2
        t2 = n+k*(3*(-k)-1)//2
        p = ((calcP3(t1)%10**6) + (calcP3(t2)%10**6)) % 10**6
        if k%2==0: Pn[n] -= p
        else: Pn[n] += p
        Pn[n] %= 10**6
    return Pn[n]


# This is a generator function, it provides a list of all the possible
# partitions for n. to see all, cast to a list. Cool to see, not too good on
# efficiency
def partitions(n,I=1):
    yield (n,)
    for i in range(I, n//2+1):
        for p in partitions(n-i,i):
            yield (i,) + p


#an attempt at something someone suggested in the thread for this problem
def part(n):
    global Pn
    while len(Pn) <= n: Pn += [0]
    if Pn[n]: return Pn[n]
    s, k, a, b, sgn = 0, 4, 2, 1, 1
    while n >= a:
        s += sgn * (Pn[n-a] + Pn[n-b])
        a += k+1
        b += k
        sgn *= -1
        k += 3
    if n >= b:
        s += sgn*Pn[n-b]
    return s%10**6

def v3():
    i=0
    while calcP3(i)!=0:
        if i == 100: print(calcP3(100))
        i+=1
        # print(calcP3(i))
    print(i)


@timer
def main():
    v3()


if __name__ == '__main__':
    main()
