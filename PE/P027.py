#Euler discovered the remarkable quadratic formula:
#n2+n+41
#It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.
#The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.
#Considering quadratics of the form:
#n2+an+b, where |a|<1000 and |b|≤1000
#where |n| is the modulus/absolute value of n
#e.g. |11|=11 and |−4|=4
#Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
import math

def isPrime(n):
    if n == 1:
        return False
        # from 1 to sqrt(n)
    for x in range(2, (int)(math.sqrt(abs(n)))+1):
        if n % x == 0:
            return False
    return True

def main():
    longestChain = 0
    la = 0;
    lb = 0;
    a = -999
    while a<1000:
        b = -1000
        while b<1001:
            n = 0;
            while(isPrime(n*n+a*n+b)):
                n = n+1
            if longestChain<n:
                longestChain = n
                la = a
                lb = b
            b = b+1
        a = a + 1
    print(la*lb)

if __name__ == '__main__':
    main()
