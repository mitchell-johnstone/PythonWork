#Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
#If we list the set of reduced proper fractions for d  8 in ascending order of size, we get:
#   1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
#   It can be seen that 2/5 is the fraction immediately to the left of 3/7.
#    By listing the set of reduced proper fractions for d  1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.
from math import *

class Fraction:
    def __init__(self,numerator,denominator):
        self.n = numerator
        self.d = denominator
    def compareTo(self,other):
        sN = self.n
        oN = other.n
        oD = other.d
        g = gcd(oN, oD)
        while g != 1:
            oN, oD = oN//g, oD//g
            g = gcd(oN, oD)
        if oN == sN and oD == self.d:
            return 0
        while(True):
            sDigit = sN*10//self.d
            sN = sN*10 % self.d
            oDigit = oN*10// oD
            oN = oN*10 % oD
            if sDigit > oDigit:
                return 1
            elif sDigit < oDigit:
                return -1


def binSearch(frac, den):
    x, y, mid = 0, den-1, 0

    while x <= y:
        mid = (x+y) // 2
        mid_frac = Fraction(mid, den)
        if frac.compareTo(mid_frac) <= 0:
            y = mid - 1
        else:
            x = mid + 1
    return y


def main():
    target = Fraction(3,7)
    best = Fraction(2,5)
    for den in range(8, 1000001):
        if den%1000 == 0:
            print(den)
        num = binSearch(target, den)
        potential_best = Fraction(num,den)
        if best.compareTo(potential_best) < 0:
            best = potential_best
    print(best.n, best.d)


if __name__ == "__main__":
    main()
