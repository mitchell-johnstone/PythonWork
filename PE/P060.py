# The primes 3, 7, 109, and 673, are quite remarkable.
# By taking any two primes and concatenating them in any order
# the result will always be prime.
# For example, taking 7 and 109, both 7109 and 1097 are prime.
# The sum of these four primes, 792, represents
# the lowest sum for a set of four primes with this property.
# 673109
# Find the lowest sum for a set of five primes
# for which any two primes concatenate to produce another prime.

#method to add a prime to the list of primes
def addPrime(primes):
    currentPrime = primes[len(primes)-1]
    while(True):
        currentPrime+=2
        if(isPrime2(currentPrime, primes)):
            primes += [currentPrime]
            print(currentPrime)
            return

# method to check if a number is prime
def isPrime(n):
    if(n%2==0):
        return False
    end = int(n**.5+1)
    for i in range(3,end,2):
        if(n%i==0):
            return False
    return True

# method to check if a number is prime
def isPrime2(n, primes):
    end = int(n**.5+1)
    for prime in primes:
        if(prime>end):
            return True
        if(n%prime==0):
            return False
    return True

#check if any two concatenated primes are also primes
def isAlwaysPrime(selection):
    for index1 in range(len(selection)):
        for index2 in range(index1+1, len(selection)):
            possible = int(str(selection[index1])+str(selection[index2]))
            if(not isPrime(possible)):
                return False
            possible = int(str(selection[index2])+str(selection[index1]))
            if(not isPrime(possible)):
                return False
    return True

def v1():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673]
    num = 5
    while(True):
        for val1 in range(len(primes)-num+1):
            for val2 in range(val1+1, len(primes)-num+2):
                for val3 in range(val2+1, len(primes)-num+3):
                    for val4 in range(val3+1, len(primes)-num+4):
                        val5 = len(primes)-1
                        indexes = [val1,val2,val3,val4, val5]
                        # print(indexes)
                        selection = [primes[x] for x in indexes]
                        # print("\t",selection)
                        if(isAlwaysPrime(selection)):
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
#find the interconnected numbers, add them up
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
                    curSum+=1
            # print(curSum)
            if not foundAlready and curSum >= target-2:
                numOverTarget+=1
                sumOverTarget += key
                # print("added ", key)
                foundAlready = True
            # print("\t",numOverTarget)
        if(numOverTarget >= target):
            return sumOverTarget
    return 0

def pairsFromPrimes(prime, primes):
    pairs = []
    prime = str(prime)
    for i in range(1,len(prime)):
        p1 = prime[:i]
        p2 = prime[i:]
        if(len(p1) + len(p2) != len(prime)):
            continue
        if(int(p1) in primes and int(p2) in primes and isPrime(int(p2+p1)) and isPrime(int(p1+p2))):
            pairs+=[[int(p1),int(p2)]]
    return pairs

def addPairsToDict(dic, pairs):
    for pair in pairs:
        #add the primes pairs
        if pair[0] not in dic:
            dic[pair[0]] = [pair[1]]
        elif pair[1] not in dic[pair[0]]:
            dic[pair[0]] += [pair[1]]

        if pair[1] not in dic:
            dic[pair[1]] = [pair[0]]
        elif pair[0] not in dic[pair[1]]:
            dic[pair[1]] += [pair[0]]
    return

#try and do the problem backwards.
# ie: for every prime, see if it is a combination of 2 primes.
# use a dictionary with the values being a key with the other primes it can be paired w/
def v2():
    primes = [2, 3, 5, 7]
    primesAndPairs = {2:[],3:[],5:[],7:[]}
    # pairsFromPrimes(,primes)
    solution = 0
    while solution == 0:
        print(primesAndPairs)
        addPrime(primes)
        currentPrime = primes[len(primes)-1]
        pairs = pairsFromPrimes(currentPrime, primes)
        if(pairs is not None):
            #add pairs to the dictionary
            addPairsToDict(primesAndPairs, pairs)

            #see if there is a solution
            solution = sufficientConnections(primesAndPairs,4)
    print(solution)

#will return a list of good connections from list of original connections
#n is current number, con is old connections
def checkConnections(n, con, sieve):
    goodConnectionsWithN = []
    for i in con:
        possiblePrime = int(string(n) + string(i))
        if not sieve[possiblePrime]:
            continue
        possiblePrime = int(string(i) + string(n))
        if not sieve[possiblePrime]:
            continue
        #since it has passed both forward and back, add to list for returning
        goodConnectionsWithN += i
    return goodConnectionsWithN

# 2019 mitchell here, back at it again with a brand new approach
# a similar concept from before but tweaked.
# Have a list that starts with a prime, then for every
# new prime, it is checked with each row and matched to all the primes in that row.
# If it doesn't work for a prime in that list, a new row is made with the primes in the list that do work.
# Have a sieve for easier checking.

def s(MAXPRIME):
    sieve = [True] * (MAXPRIME+1)
    sieve[0] = sieve[1] = False
    for n in range(2, int((MAXPRIME+1)**.5+1)):
        if(sieve[n]):
            #we've encountered a prime!
            for c in range(n**2, MAXPRIME+1, n):
                sieve[c] = False
    return sieve

def v3():
    MAXPRIME = 1000000
    sieve = s(MAXPRIME)
    connections = [[2,3],[3,2,5],[3,5],[3,7,11]]
    print(connections)
    connections = sorted(connections)
    print(connections)

# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321]
def main():
    v3()
    return

if __name__ == '__main__':
    main()
