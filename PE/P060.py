# The primes 3, 7, 109, and 673, are quite remarkable.
# By taking any two primes and concatenating them in any order
# the result will always be prime.
# For example, taking 7 and 109, both 7109 and 1097 are prime.
# The sum of these four primes, 792, represents
# the lowest sum for a set of four primes with this property.
# 673109
# Find the lowest sum for a set of five primes
# for which any two primes concatenate to produce another prime.

import numpy as np
import itertools as i
import time


# method to add a prime to the list of primes
def addPrime(primes):
    currentPrime = primes[len(primes) - 1]
    while (True):
        currentPrime += 2
        if (isPrime2(currentPrime, primes)):
            primes += [currentPrime]
            print(currentPrime)
            return


# method to check if a number is prime
def isPrime(n):
    if (n % 2 == 0):
        return False
    end = int(n ** .5 + 1)
    for i in range(3, end, 2):
        if (n % i == 0):
            return False
    return True


# method to check if a number is prime
def isPrime2(n, primes):
    end = int(n ** .5 + 1)
    for prime in primes:
        if (prime > end):
            return True
        if (n % prime == 0):
            return False
    return True


# check if any two concatenated primes are also primes
def isAlwaysPrime(selection):
    for index1 in range(len(selection)):
        for index2 in range(index1 + 1, len(selection)):
            possible = int(str(selection[index1]) + str(selection[index2]))
            if (not isPrime(possible)):
                return False
            possible = int(str(selection[index2]) + str(selection[index1]))
            if (not isPrime(possible)):
                return False
    return True


def v1():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
              107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
              227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347,
              349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
              467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
              613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673]
    num = 5
    while (True):
        for val1 in range(len(primes) - num + 1):
            for val2 in range(val1 + 1, len(primes) - num + 2):
                for val3 in range(val2 + 1, len(primes) - num + 3):
                    for val4 in range(val3 + 1, len(primes) - num + 4):
                        val5 = len(primes) - 1
                        indexes = [val1, val2, val3, val4, val5]
                        # print(indexes)
                        selection = [primes[x] for x in indexes]
                        # print("\t",selection)
                        if (isAlwaysPrime(selection)):
                            print(selection)
                            print()
                            print(sum(selection))
                            return
        addPrime(primes)
        print(primes)
        # if(primes[len(primes)-1]>674):
        #     print("error")
        #     return


# I think this part needs work. too confusing.
# find the interconnected numbers, add them up
def sufficientConnections(primesAndPairs, target):
    sumOverTarget = 0
    numOverTarget = 0
    for key in primesAndPairs:
        pairs = primesAndPairs[key]
        foundAlready = False
        # print(pairs)
        for pairKey in pairs:
            curSum = 0
            for pairCompare in pairs:
                if pairCompare in primesAndPairs[pairKey]:
                    curSum += 1
            # print(curSum)
            if not foundAlready and curSum >= target - 2:
                numOverTarget += 1
                sumOverTarget += key
                # print("added ", key)
                foundAlready = True
            # print("\t",numOverTarget)
        if (numOverTarget >= target):
            return sumOverTarget
    return 0


def pairsFromPrimes(prime, primes):
    pairs = []
    prime = str(prime)
    for i in range(1, len(prime)):
        p1 = prime[:i]
        p2 = prime[i:]
        if (len(p1) + len(p2) != len(prime)):
            continue
        if (int(p1) in primes and int(p2) in primes and isPrime(int(p2 + p1)) and isPrime(int(p1 + p2))):
            pairs += [[int(p1), int(p2)]]
    return pairs


def addPairsToDict(dic, pairs):
    for pair in pairs:
        # add the primes pairs
        if pair[0] not in dic:
            dic[pair[0]] = [pair[1]]
        elif pair[1] not in dic[pair[0]]:
            dic[pair[0]] += [pair[1]]

        if pair[1] not in dic:
            dic[pair[1]] = [pair[0]]
        elif pair[0] not in dic[pair[1]]:
            dic[pair[1]] += [pair[0]]
    return


# try and do the problem backwards.
# ie: for every prime, see if it is a combination of 2 primes.
# use a dictionary with the values being a key with the other primes it can be paired w/
def v2():
    primes = [2, 3, 5, 7]
    primesAndPairs = {2: [], 3: [], 5: [], 7: []}
    # pairsFromPrimes(,primes)
    solution = 0
    while solution == 0:
        print(primesAndPairs)
        addPrime(primes)
        currentPrime = primes[len(primes) - 1]
        pairs = pairsFromPrimes(currentPrime, primes)
        if (pairs is not None):
            # add pairs to the dictionary
            addPairsToDict(primesAndPairs, pairs)

            # see if there is a solution
            solution = sufficientConnections(primesAndPairs, 4)
    print(solution)


# will return a list of good connections from list of original connections
# n is current number, con is old connections
def checkConnections(n, con, sieve):
    goodConnectionsWithN = []
    for i in con:
        possiblePrime = int(string(n) + string(i))
        if not sieve[possiblePrime]:
            continue
        possiblePrime = int(string(i) + string(n))
        if not sieve[possiblePrime]:
            continue
        # since it has passed both forward and back, add to list for returning
        goodConnectionsWithN += i
    return goodConnectionsWithN


# 2019 mitchell here, back at it again with a brand new approach
# a similar concept from before but tweaked.
# Have a list that starts with a prime, then for every
# new prime, it is checked with each row and matched to all the primes in that row.
# If it doesn't work for a prime in that list, a new row is made with the primes in the list that do work.
# Have a sieve for easier checking.

def s(MAXPRIME):
    sieve = [True] * (MAXPRIME + 1)
    sieve[0] = sieve[1] = False
    for n in range(2, int((MAXPRIME + 1) ** .5 + 1)):
        if (sieve[n]):
            # we've encountered a prime!
            for c in range(n ** 2, MAXPRIME + 1, n):
                sieve[c] = False
    return sieve


def s2(MAXPRIME):
    sieve = np.array([True for i in range(MAXPRIME + 1)], dtype=bool)
    sieve[0] = sieve[1] = False
    # print(sieve)
    for n in range(2, int((MAXPRIME + 1) ** .5 + 1)):
        if (sieve[n]):
            # we've encountered a prime!
            for c in range(n ** 2, MAXPRIME + 1, n):
                sieve[c] = False
    return sieve


# function to see if 2 primes can be concatenated
def conc(a, b, sieve):
    num1 = int(str(a) + str(b))
    num2 = int(str(b) + str(a))
    if num1 < len(sieve) and num2 < len(sieve):
        if sieve[num1] and sieve[num2]:
            return True
    return False


def v3(MAXPRIME, target):
    print(MAXPRIME)
    sieve = s2(MAXPRIME)
    # print(conc(3, 7, sieve))
    primes = []
    for i in range(len(sieve)):
        if (sieve[i]):
            primes += [i]

    start = time.time()

    maxIntLen = len(str(MAXPRIME))
    connections = {}
    for i in primes:
        connections[i] = [i]
        curMax = maxIntLen - len(str(i))
        for j in primes:
            if (len(str(j)) > curMax):
                break
            num1 = int(str(i) + str(j))
            num2 = int(str(j) + str(i))
            if num1 < MAXPRIME and num2 < MAXPRIME:
                if sieve[num1] and sieve[num2]:
                    connections[i] += [j]

    connections = {k: v for k, v in connections.items() if len(v) >= target}

    print("All good combinations found, looking for the perfect sum...")

    # look for the smallest sum
    if target == 4:
        for key in connections.keys():
            upTo = len(connections[key])
            for i1 in range(1, upTo):
                for i2 in range(i1 + 1, upTo):
                    for i3 in range(i2 + 1, upTo):
                        try:
                            v1 = connections[key][i1]
                            v2 = connections[key][i2]
                            v3 = connections[key][i3]
                            if (v1 in connections[v2] and v1 in connections[v3] and v2 in connections[v3]):
                                print(key + v1 + v2 + v3)
                                return True
                        except KeyError:
                            "Skipped"
                            continue
    elif target == 5:
        for key in connections.keys():
            upTo = len(connections[key])
            for i1 in range(1, upTo):
                v1 = connections[key][i1]
                if v1 not in connections.keys():
                    break
                for i2 in range(i1 + 1, upTo):
                    v2 = connections[key][i2]
                    if v2 not in connections.keys():
                        break
                    for i3 in range(i2 + 1, upTo):
                        v3 = connections[key][i3]
                        if v3 not in connections.keys():
                            break
                        for i4 in range(i3 + 1, upTo):
                            v4 = connections[key][i4]
                            if v4 not in connections.keys():
                                break
                            if ((v1 in connections[v2] and v1 in connections[v3] and v1 in connections[v4] and v2 in
                                 connections[v3] and v2 in connections[v4] and v3 in connections[v4])):
                                print(key + v1 + v2 + v3 + v4)

                                end = time.time()
                                print("Final answer took " + str(int(end - start)) + " seconds")
                                return True
    print("Sorry, princess is in a different castle :(")
    end = time.time()
    print("No answer took " + str(int(end - start)) + " seconds")
    return False


def main():
    target = 5
    if not v3(99999, target):
        if not v3(999999, target):
            if not v3(9999999, target):
                if not v3(99999999, target):
                    if not v3(999999999, target):
                        if not v3(9999999999, target):
                                print("Big Problem")
    return


if __name__ == '__main__':
    main()
