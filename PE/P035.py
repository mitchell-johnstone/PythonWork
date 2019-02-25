# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?
primes = [2,3]

def PrimesToN(n):
    global primes
    while (primes[len(primes)-1]<n):
        addPrime()
        # print(primes[len(primes)-1])
    primes.remove(primes[len(primes)-1])


def addPrime():
    global primes
    l = len(primes)
    current = primes[len(primes)-1]+2
    while l == len(primes):
        prime = True
        i = 0
        while (i < l and prime):
            p=primes[i]
            if current%p==0:
                prime=False
            i+=1
        if(prime):
            primes += [current]
        else:
            current+=2

def main():
    global primes
    target = 1000000
    PrimesToN(target)
    countOfPrimes = 0
    for possibleCircularPrime in primes:
        shufflePrime = str(possibleCircularPrime)
        shufflePrime = shufflePrime[len(shufflePrime)-1] + shufflePrime[0:len(shufflePrime)-1]
        # print(shufflePrime)
        prime = int(shufflePrime) in primes
        while(shufflePrime != str(possibleCircularPrime) and prime):
            shufflePrime = shufflePrime[len(shufflePrime)-1] + shufflePrime[0:len(shufflePrime)-1]
            prime = int(shufflePrime) in primes
        if(prime):
            countOfPrimes+=1
            # print(possibleCircularPrime)
    print()
    print(countOfPrimes)

if __name__ == "__main__":
    main()
