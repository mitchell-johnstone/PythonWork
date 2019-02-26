# The number 3797 has an interesting property.
# Being prime itself, it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7.
# Similarly we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

# list to hold prime numbers
primes = [2,3,5,7]

#function to add a prime to list
def addPrime():
    global primes
    # l is the original length, to check with updated length
    l = len(primes)
    #never will be even, so current always adds 2
    current = primes[len(primes)-1]+2
    while l == len(primes):
        prime = True
        i = 0
        while (i < l and prime):
            p=primes[i]
            #if divisible by a prime, then it's not prime
            if current%p==0:
                prime=False
            i+=1
        if(prime):
            primes += [current]
            return current
        else:
            current+=2

# a method to truncate from the left
def tLeft(n):
    n=str(n)
    return (n[1:])

# a method to truncate from the right
def tRight(n):
    n=str(n)
    return (n[:len(n)-1])

def isTruncatable(n):
    global primes
    n = str(n)
    #copy n to modify n
    original = n
    #check truncating from right
    while len(n)>1:
        n=tRight(n)
        # print(n)
        i = int(n)
        if i not in primes:
            return False
    #reset n
    n=original
    #check truncating from left
    while len(n)>1:
        n=tLeft(n)
        # print(n)
        i = int(n)
        if i not in primes:
            return False
    #if both have been passed through,
    #it is a truncatable prime
    return True

def main():
    global primes
    # list to hold good primes
    truncatablePrimes = []
    while len(truncatablePrimes)<11:
        # get the prime added to the list
        currentP = addPrime()
        # print(currentP)
        # check if it is truncatable
        if isTruncatable(currentP):
            truncatablePrimes+=[currentP]
            print(currentP)
    print()
    print(sum(truncatablePrimes))

if __name__ == '__main__':
    main()
