# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

def addPrime(ps):
    #get the last prime added
    currentPrime = ps[len(ps)-1]

    #loop until we get a new prime number
    while(True):
        #assume it's true
        primeN = True

        # all primes that are not 2 are odd
        currentPrime+=2

        #index holder
        i = 0
        while(primeN and i<len(ps) and ps[i] < (currentPrime**.5) + 1):

            #check if the current prime divides into the possible prime
            if(currentPrime % ps[i] == 0):
                primeN = False

            #increment
            i+=1

        if(primeN):
            return ps + [currentPrime]

# for this problem, I don't just want to import the whole primes list.
# instead, I'll just add when needed.
# this way, I can use the sum() method for lists
def main():
    primes = [2,3]

    #get the target number
    target = int(input("""What is the target?"""))

    #var to hold all primes up to 1 mil
    AllPrimes = []
    f = open("C:\\Users\\Admin\\Documents\\Coding\\Python\\PE\\AllPrimes.txt")

    # import the primes needed
    for line in f:
        words = line.split();
        for word in words:
            if(int(word)<1000000):
                AllPrimes+=[int(word)]

    #var to hold the last prime
    #var to hold the longest length
    longestPrime = 0
    longestLength = 0

    #loop through until the last index has a number over the target.
    #that way, any sum with it in will just go over the target
    while(sum(primes[len(primes)-longestPrime:])<target):

        #loop through all the indexes of primes
        i = 0
        while(i<len(primes)):

            if(len(primes[i:])<longestLength):
                i=len(primes)
            else:
                #add up all primes from i forward
                tmpSum = sum(primes[i:])

                #check that the sum is under the target
                #check that the sum is prime
                if(tmpSum < target and tmpSum in AllPrimes):

                    #check if the length has been surpassed
                    if(len(primes[i:]) > longestLength):

                        #adjust longest lengths and new prime
                        longestLength = len(primes[i:])
                        longestPrime = sum(primes[i:])

            #increment the index
            i+=1

        #add a prime to continue
        primes = addPrime(primes)
        # print(primes[len(primes)-1])

    # print results
    print("""Longest Prime: """,longestPrime)
    print("""Length : """, longestLength)
if __name__ == "__main__":
    main()
