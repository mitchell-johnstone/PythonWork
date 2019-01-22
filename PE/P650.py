import math
import scipy.special
import time
from functools import reduce

def fac(n):
    sum=1
    for i in range(n):
        i+=1
        sum*=i
    return sum

def comb(n,r):
    # since C(n, k) = C(n, n - k)
    if(r > n - r):
        r = n - r
    # initialize result
    res = 1
    # Calculate value of
    # [n * (n-1) *---* (n-k + 1)] / [k * (k-1) *----* 1]
    for i in range(r):
        res = res * (n - i)
        res = res / (i + 1)
    return res

    # return fac(n)/(fac(r)*fac(n-r))
    return scipy.special.comb(n,r,exact=True)

def B(n):
    # l=[]
    # for i in range(n+1):
    #     l+=[comb(n,i)]
    # sum = 1
    # for i in range(len(l)):
    #     sum*=l[i]
    sum = 1
    for i in range(1,n+1):
        sum *= comb(n,i)
    return sum

def D(n):
    sum = 0
    t = int(math.sqrt(n))
    for i in range(1,t+1):
        if (n%i==0):
            sum += i
            sum += n//i
            # if sum>1000000007:
            #     sum=sum%1000000007
            if i==t:
                sum-=t
    return sum

def S(n):
    sum = 1;
    for i in range(n):
        i+=1
        t= D((int)(B(i)))
        sum+=t
        print(t)
        # if sum>1000000007:
        #     sum = sum%1000000007
    return sum

def isPrime(n):
    for i in range(2,int(n**.5)+1):
        if(n%i==0):
            return False
    return True

def findFactors(n):
    l = []
    i=2
    # t = int(n**.5)+1
    while (n>1):
        if(n%i==0):
            l+=[i]
            n=n/i
            i-=1
        i+=1
    # print(l)
    return l;

def tmp(n):
    if(n<2):
        return 1
    l = []
    for i in range(1,n):
        t = comb(n,i)
        if(isPrime(t)):
            l+=[t]
        else:
            t = findFactors(t)
            l+=t
    l.sort()
    # print(l)
    factors = [[l[0],0]]
    current = 0
    for i in l:
        i = int(i)
        if i==factors[current][0]:
            factors[current][1]+=1
        else:
            factors += [[i,1]]
            current+=1
    # for i in l:
    #     i = int(i)
    #     found = False
    #     k=0
    #     while((k<len(factors)) and (not found)):
    #         if (factors[k][0] == i):
    #             factors[k][1]+=1
    #             found = True
    #         k+=1
    #     if(not found):
    #         factors += [[i,0]]

    print(factors)
    sum = 1;

    vals = [0]*len(factors)
    tmpIndex = len(vals)-1
    vals[tmpIndex]+=1
    while not vals[0]>factors[0][1]:
        # print(vals)
        tmpSum = 1;
        for i in range(len(vals)):
            tmpSum=tmpSum*(factors[i][0]**vals[i])
        if(tmpSum>1):
            sum+=tmpSum
        tmpIndex = len(vals)-1
        vals[tmpIndex]+=1
        while tmpIndex>0:
            if(vals[tmpIndex]>factors[tmpIndex][1]):
                vals[tmpIndex] = 0
                vals[tmpIndex-1] +=1
            tmpIndex-=1


    # multiples = []
    # for i in range(2**len(l)):
    #     print(i)
    #     tmp = len(binary)-1
    #     binary[tmp]+=1
    #     while(tmp>0):
    #         if(binary[tmp]>1):
    #             binary[tmp]=0
    #             binary[tmp-1]+=1
    #         tmp-=1
    #     sum = 1
    #     for i in range(len(binary)):
    #         if(binary[i]==1):
    #             sum*=l[i]
    #     if(sum not in multiples):
    #         multiples+=[sum]
    # sum = 0
    # for i in range(len(multiples)):
    #     sum+=multiples[i]
    return sum

def pascal(n):
    line = [1]
    for k in range(n):
        line.append(line[k]*(n-k)/(k+1))
    return line

def VThree(n):
    if(n<2):
        return 1
    factors = {}
    nextBinomial = 1
    # t = pascal(n)
    for i in range(n):
        nextBinomial = nextBinomial*(n-i)/(i+1)
        l = findFactors(nextBinomial)
        for possibleFactor in l:
            if(not possibleFactor in factors):
                factors[possibleFactor]=0
            factors[possibleFactor]+=1
    # for i in range(1,n):
    #     t = comb(n,i)
    #     t = findFactors(t)
    #     for l in t:
    #         if(not l in factors):
    #             factors[l]=0
    #         factors[l]+=1
    print(factors)
    vals = [0]*len(factors)
    tmpIndex = len(vals)-1
    vals[tmpIndex]+=1
    keys = list(factors.keys())
    sum = 1
    while not vals[0]>factors[keys[0]]:
        tmpSum = 1;
        for i in range(len(vals)):
            tmpSum=tmpSum*(keys[i]**vals[i])
        tmpSum=tmpSum%1000000007
        if(tmpSum>1):
            sum+=tmpSum
        tmpIndex = len(vals)-1
        vals[tmpIndex]+=1
        while tmpIndex>0:
            if(vals[tmpIndex]>factors[keys[tmpIndex]]):
                vals[tmpIndex] = 0
                vals[tmpIndex-1] +=1
            tmpIndex-=1
    return sum

def factors_2(n):
    step = 2 if n%2 else 1
    return set(reduce(list.__add__,
                ([i,n//i] for i in range(1,int(math.sqrt(n))+1, step) if n%i==0)))

def V4(n):
    BSum = 1
    nextBinomial = 1
    for i in range(n):
        nextBinomial = nextBinomial*(n-i)/(i+1)
        BSum *= nextBinomial
    factors = factors_2(BSum)
    sum =  0
    for i in factors:
        sum += i
    return sum

# primes = []
# file = open("Primes.txt", "r")
# f1 = file.readlines()
# for x in f1:
#     l = x.split()
#     for p in l:
#         primes += [int(p)]
# print(primes)

def V5(n):
    if(n<2):
        return 1
    factors = {}
    nextBinomial = 1
    # binomialProduct = 1
    print(n)
    for i in range(n):
        # print(str(i)+" C "+str(n))
        # print((n-i)/(i+1))
        nextBinomial = nextBinomial*(n-i)/(i+1)
        # binomialProduct*=nextBinomial
        l = findFactors(nextBinomial)
        for possibleFactor in l:
            if(not possibleFactor in factors):
                factors[possibleFactor]=0
            factors[possibleFactor]+=1
        # print(factors)
    # print(binomialProduct)
    # i=0
    # t = math.sqrt(binomialProduct)+1
    # while(primes[i]<t):
    #     if(binomialProduct%primes[i]==0):
    #         if(not primes[i] in factors):
    #             factors[primes[i]]=0
    #         factors[primes[i]]+=1
    #         binomialProduct=binomialProduct//primes[i]
    #         i-=1
            # print(factors)
        # i+=1
    # print("done with factors")
    sum = 1
    keys = list(factors.keys())
    for key in keys:
        tmpSum = 1
        for exp in range(1,factors[key]+1):
            tmpSum += key**exp
        sum*=tmpSum
    return sum

def V6(n):
    if(n<2):
        return 1
    factors = {}
    nextBinomial = 1
    for i in range(n):
        nextBinomial = nextBinomial*(n-i)/(i+1)
        # l = findFactors(nextBinomial)
        # for possibleFactor in l:
        #     if(not possibleFactor in factors):
        #         factors[possibleFactor]=0
        #     factors[possibleFactor]+=1
        temp = nextBinomial
        if temp%2==0:
            factors[2]=0
            while(temp%2==0):
                factors[2]+=1
                temp=temp//2
        current = 3
        # print("past 2")
        while temp>1:
            if temp%current==0:
                if not current in factors:
                    factors[current]=0
                factors[current]+=1
                temp=temp//current
                current-=2
            current+=2
    print("found all factors")
    print(factors)
    sum = 1
    keys = list(factors.keys())
    for key in keys:
        tmpSum = 1
        for exp in range(1,factors[key]+1):
            tmpSum += key**exp
        sum*=tmpSum
    return sum

def main():
    x = input("How high?")
    print(comb(55,26))
    # 3085851035479212.0
    # 3085851035479212.0
    # input("Continue?")
    start = time.time()
    sum = 0
    for i in range(1,1+int(x)):
        # print(i)
        t = int(V5(i))
        sum+=t
        print(t)
    print()
    # sum=sum%1000000007
    print(sum)
    end = time.time()
    print("This operation took " + str(end-start) + " seconds")
    # start = time.time()
    # sum = 0
    # for i in range(1,1+int(x)):
    #     t=int(VThree(i))
    #     sum+=t
    #     print(t)
    #     sum=sum%1000000007
    # print()
    # print("Sum is: " + str(sum))
    # end = time.time()
    # print("Time operation took:")
    # print(end-start)
    # print()
    # start = time.time()
    # sum=0
    # for i in range(1,1+int(x)):
    #     t=int(tmp(i))
    #     sum+=t
    #     print(t)
    #     sum=sum%1000000007
    # print()
    # print("Sum is: " + str(sum))
    # end = time.time()
    # print("Time operation took:")
    # print(end-start)
    # print(S(int(x)))
    # print(S(20000))

if __name__ == '__main__':
    main()
