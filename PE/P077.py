# It is possible to write ten as the sum of primes in exactly five different ways:
# 7 + 3
# 5 + 5
# 5 + 3 + 2
# 3 + 3 + 2 + 2
# 2 + 2 + 2 + 2 + 2
# What is the first value which can be written
# as the sum of primes in over five thousand different ways?
from decorators import *
import numpy as np
import math


primes = []
def generatePrimeList():
    global primes
    f = open("AllPrimes.txt")
    for line in f.readlines():
        # print(line)
        primes += [int(i) for i in line.split(" ") if i and i != "\n"]
    #print(primes)
    f.close()


def sopf(n):
    global primes
    sum = 0
    for p in primes:
        divides = False
        while n%p==0:
            n//=p
            divides = True
        if divides:
            sum += p
        if n == 1: break
    return sum


k=[0]*1000
def calcK(n):
    if n==0 or k[n]: return k[n]
    s1 = sopf(n)
    s2 = sum([sopf(j)*calcK(n-j) for j in range(1,n)])
    k[n] = (s1+s2)//n
    return k[n]


def v1():
    generatePrimeList()
    i = 2
    while calcK(i) <= 5000:
        i+=1
    print(i)


@timer
def main():
    v1()


if __name__ == '__main__':
    main()
