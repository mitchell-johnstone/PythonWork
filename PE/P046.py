# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

def addSquare(ps):
    return ps + [(1+len(ps))**2]

def addPrime(p):
    c = p[len(p)-1]
    while True:
        c+=2
        currentlyPrime = True
        i = 0
        prime = p[i]
        while i < len(p) and (p[i] < 1+c**.5) and currentlyPrime:
            if(c % p[i] == 0):
                currentlyPrime = False
            i+=1
        if(currentlyPrime):
            return p + [c]

# (odd - prime) / 2 == perfect square
def main():
    #array to hold perfect squares
    perfectSquares = [1,4]

    #variable to hold the current odd value
    curOdd = 7

    #array to hold Primes
    primes = [2,3]

    # loop until the conjecture is false
    while(True):
        #get to next odd number
        curOdd+=2

        #add primes until we get above the current number
        while(primes[len(primes)-1] < curOdd):
            primes = addPrime(primes)

        #if its not a prime, then calculate
        if curOdd not in primes:

            #variable to see if the conjecture it ture
            satisfies = False
            pIndex = 0

            #loop for all primes under
            while(pIndex<len(primes) and not satisfies):
                if(primes[pIndex]<curOdd):
                    #possible perfect square
                    pps = (curOdd-primes[pIndex])//2

                    while (pps>perfectSquares[len(perfectSquares)-1]):
                        perfectSquares = addSquare(perfectSquares)
                    if pps in perfectSquares:
                        satisfies = True
                pIndex+=1
            if(not satisfies):
                print(curOdd)
                return

if __name__ == '__main__':
    main()
