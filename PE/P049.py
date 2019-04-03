# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by
# 3330, is unusual in two ways: (i) each of the three terms are prime, and,
# (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
# exhibiting this property, but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?

def isPermutation(pn1,pn2,pn3):
    #strings easier to permute.
    p1 = str(pn1)
    p2 = str(pn2)
    p3 = str(pn3)

    #take the strings, change them to sorted list
    digits1 = sorted(list(p1))
    digits2 = sorted(list(p2))
    digits3 = sorted(list(p3))

    #loop through all the digits of the first number,
    # comparing them to the second and third
    #since we sorted the lists, the digits should be exactly the same
    for i in range(len(digits1)):
        if(digits1[i] != digits2[i] or digits1[i] != digits3[i]):
            return False

    #if both other numbers are permutations of the first,
    # return True
    return True

def main():
    print(isPermutation(1487,4817,8147))
    # return
    primes = []
    f = open("C:/Users/Admin/Documents/Coding/Python/PE/Primes.txt", "r")
    # import the primes needed
    for line in f:
        words = line.split();
        for word in words:
            if(int(word)>999 and int(word)<10000):
                primes+=[int(word)]

    # start at bottom of the primes that are 4 digits
    for lowPrime in range(len(primes)):
        # print(primes[lowPrime])

        #get the next prime, go all the way to the top
        for medPrime in range(lowPrime+1 , len(primes)):
            # print("\t",primes[medPrime])

            #find difference between 1 and 2, then add that back to 2
            difference = primes[medPrime] - primes[lowPrime]
            highPrime = primes[medPrime] + difference

            #check if the new posssible prime is a prime
            if(highPrime in primes):

                #check if all the numbers are permutations of each other
                if(isPermutation(primes[lowPrime],primes[medPrime],highPrime)):

                    #if passed through, print them all
                    print(primes[lowPrime], primes[medPrime], highPrime)

if __name__ == '__main__':
    main()
