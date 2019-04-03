# By replacing the 1st digit of the 2-digit number *3,
# it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
#
# By replacing the 3rd and 4th digits of 56**3 with the same digit,
# this 5-digit number is the first example having seven primes
# among the ten generated numbers, yielding the family:
# 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
# Consequently 56003, being the first member of this family,
# is the smallest prime with this property.
#
# Find the smallest prime which, by replacing part of the number
# (not necessarily adjacent digits) with the same digit,
# is part of an eight prime value family.

# general notes:
# can never replace the last digit.
# otherwise, it'll be a family of max 5 primes.
# if replacing the first digit, don't use 0.


#this methods finds the indexes of the different digits
#return a list of digits and where they are in the number
#indexes = digit, -1 = digit not present
def findSimilarDigits(n):
    #10 possible digits
    digits = [[-1]]*10
    # print(digits)

    n=str(n)
    index = 0
    while(index<len(n)):
        digit = int(n[index])

        if(digits[digit] == [-1]):
            digits[digit] = [index]
        else:
            digits[digit] += [index]

        #the last digit will only have 5 possible primes. all others are even.
        #thus, change
        if(index == len(n)-1):
            digits[digit] = [-1]

        index+=1
    return digits

#method to return an array with the family of numbers
#parameters: original number, indexes to replace
def family(n, indexes):
    n = str(n)
    members = []
    if indexes[0] == -1:
        return []
    start = 0
    if(indexes[0] == 0):
        start = 1
    for digit in range(start, 10):
        for index in indexes:
            n = n[:index] + str(digit) + n[index+1:]
        members += [int(n)]
    return members

def main():
    #var to hold all primes up to 1 mil
    AllPrimes = []
    f = open("C:\\Programming\\Work\\Python\\PE\\AllPrimes.txt")

    # import the primes needed
    for line in f:
        words = line.split();
        for word in words:
            if(int(word)<100000000 and int(word)>10):
                AllPrimes+=[int(word)]

    #loop through all primes
    for prime in AllPrimes:

        #get digits of the prime
        digits = findSimilarDigits(prime)
        # print(prime)
        #for every prime, find the family
        for i in range(10):
            fam = family(prime, digits[i])
            if(fam == []):
                continue
            # print(fam)
            familySize = 0
            indexForPrime = 0
            for member in fam:
                while(indexForPrime < len(AllPrimes)-1 and AllPrimes[indexForPrime] < member):
                    indexForPrime+=1
                if(AllPrimes[indexForPrime] == member):
                    familySize+=1
            if(familySize == 8):
                print("\n",fam)
                return
    print()

if __name__ == '__main__':
    main()
