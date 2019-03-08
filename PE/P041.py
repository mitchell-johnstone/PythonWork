# We shall say that an n-digit number is pandigital if it makes use of
# all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

import math

primes = [2,3]

def addPrime():
    global primes
    l = len(primes)
    current = primes[len(primes)-1]+2
    while l == len(primes):
        prime = True
        i = 0
        while (primes[i] < math.sqrt(current)+1 and prime):
            p=primes[i]
            if current%p==0:
                prime=False
            i+=1
        if(prime):
            primes += [current]
            p = open("C:/Users/Admin/Documents/Coding/Python/PE/Primes.txt", "a")
            p.write(str(current) + "\n")
        else:
            current+=2


def isPandigital(n):
    n = str(n)
    #var to hold the digits
    digits = []

    #len of n gives the number of digits
    for i in range(1,len(n)+1):
        digits+=[str(i)]

    #go through n to see if every digit in digits is there
    for digit in digits:
        if digit not in n:
            return False
    #if all digits are in number, then return true
    return True

def main():
    # array to hold the primes
    global primes

    #load in Primes
    f = open("C:/Users/Admin/Documents/Coding/Python/PE/Primes.txt", "r")
    work_data = f.readlines()
    for line in work_data:
        words = line.split()
        for word in words:
            primes+=[int(word)]

    #var to have the current number
    cur = primes[0]

    i = 1
    while i < len(primes):
        # print(cur)
        if(isPandigital(cur)):
            print("\t",cur)
        cur = primes[i]
        i+=1
        if(i == len(primes)):
            addPrime();
        if(cur>7654321):
            return

if __name__ == '__main__':
    main()
