# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

import math

def nonTrivial1(n,d):
    n=str(n)
    d=str(d)
    # if(n[0] == d[0]):
    #     if(not d[1] == '0'):
    #         return int(n[1])/int(d[1])
    if(n[0] == d[1]):
        if(not d[0] == '0'):
            return int(n[1])/int(d[0])
    return 1

def nonTrivial2(n,d):
    n=str(n)
    d=str(d)
    if(n[1] == d[0]):
        if(not d[1] == '0'):
            return int(n[0])/int(d[1])
    # if(n[1] == d[1]):
    #     if(not d[0] == '0'):
    #         return int(n[0])/int(d[0])
    return 1

def simplify(n,d):
    nFactors = []
    dFactors = []
    count = 2
    while n>1:
        if(n%count==0):
            nFactors+=[count]
            n//=count
            count-=1
        count+=1
    count = 2
    while d>1:
        if(d%count==0):
            dFactors += [count]
            d//=count
            count-=1
        count+=1
    for nFactor in range(len(nFactors)):
        for dFactor in range(len(dFactors)):
            if(nFactors[nFactor]==dFactors[dFactor]):
                nFactors[nFactor]=1
                dFactors[dFactor]=1
    nSum = 1
    for nFactor in nFactors:
        nSum*=nFactor
    dSum = 1
    for dFactor in dFactors:
        dSum *= dFactor
    print()
    print("Final Fraction")
    print(str(nSum)+" / "+str(dSum))

def main():
    numeratorProduct = 1
    denominatorProduct=1
    for denominator in range(11,100):
        for numerator in range(10,denominator):
            fraction = numerator/denominator
            if (fraction == nonTrivial1(numerator,denominator) or fraction == nonTrivial2(numerator,denominator)):
                numeratorProduct*=numerator
                denominatorProduct*=denominator
                print(str(numerator)+ " / " + str(denominator))
    simplify(numeratorProduct, denominatorProduct)
    print()

if __name__ == '__main__':
    main()
