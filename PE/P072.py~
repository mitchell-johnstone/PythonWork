# Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
# If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:
#   1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# It can be seen that there are 21 elements in this set.
# How many elements would be contained in the set of reduced proper fractions for d <= 1,000,000?
import math
from P070 import phi

def reduced(num, den):
    return math.gcd(num,den) == 1


def maxNum(den, targetN, targetD):
    return math.floor((den*targetN - 1) / targetD)


def minNum(den, targetN, targetD):
    return math.ceil((den*targetN + 1) / targetD)


def v1():
    count = 0
    maxD = 10**6
    for curDen in range(2,maxD+1):
        count+=1
        for curNum in range(2, curDen):
            if reduced(curNum, curDen):
                # print(curNum, " ", curDen)
                count+=1
    print(count)


def v2():
    print(sum([phi(n) for n in range(2,10**6+1)]))
    

def main():
    v2()

if __name__ == "__main__":
    main()
