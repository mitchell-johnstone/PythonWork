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
    n=int(n)
    if(n<2):
        return 1
    factors = {}
    nextBinomial = 1
    for i in range(n-1):
        # print(i+1)
        nextBinomial = nextBinomial * (n-i) // (i+1)
        # print(nextBinomial)
        temp = nextBinomial
        if temp%2==0:
            if(2 not in factors):
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
    # print("found all factors")
    # print(factors)
    sum = 1
    keys = list(factors.keys())
    for key in keys:
        tmpSum = 1
        for exp in range(1,factors[key]+1):
            tmpSum += key**exp
        sum*=tmpSum
    return sum

def V7(n):
    n=int(n)
    if(n<2):
        return 1
    factors = {}
    nextBinomial = 1
    i = 1
    start = time.time()
    while i <= int((n-1)/2):
        # print(i+1)
        nextBinomial = nextBinomial * (n-i+1) // (i)
        # print(nextBinomial)
        temp = nextBinomial
        if temp%2==0:
            if(2 not in factors):
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
        i+=1
    for key in factors:
        factors[key]=factors[key]*2
    if n%2==0:
        # print(i+1)
        nextBinomial = nextBinomial * (n-i+1) // (i)
        # print(nextBinomial)
        temp = nextBinomial
        if temp%2==0:
            if(2 not in factors):
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
    end = time.time()
    # print("Factors: " + str(end-start))
    # print("found all factors")
    # print(factors)
    sum = 1
    keys = list(factors.keys())
    start = time.time()
    for key in keys:
        tmpSum = 1
        for exp in range(1,factors[key]+1):
            tmpSum += key**exp
            tmpSum=tmpSum%1000000007
        if tmpSum == 0:
            return 0
        sum*=tmpSum
        sum=sum%1000000007
    # print(sum)
    # end = time.time()
    # print("Sum: " + str(end-start))
    return sum

primes = [2,3]

def PrimesTo20000():
    global primes
    while (primes[len(primes)-1]<20000):
        addPrime()

def addPrime():
    global primes
    l = len(primes)
    current = primes[len(primes)-1]+2
    while l == len(primes):
        prime = True
        i = 0
        while (i < l and prime):
            p=primes[i]
            if current%p==0:
                prime=False
            i+=1
        if(prime):
            primes += [current]
        else:
            current+=2

#currently 8 is fastest
def V8(n):
    global primes
    n=int(n)
    if(n<2):
        return 1
    factors = {}
    nextBinomial = 1
    i = 1
    start = time.time()
    #do first half of binomialProducts
    while i <= int((n-1)/2):
        #find next binomial from past binomial
        nextBinomial = nextBinomial * (n-i+1) // (i)
        temp = nextBinomial
        l = 0
        while(temp > 1):
            if temp%primes[l]==0:
                if not primes[l] in factors:
                    factors[primes[l]] = 0
                factors[primes[l]]+=1
                temp=temp//primes[l]
                l-=1
            l+=1
            #if we've run out of primes, add we still are over 1,
            # add another prime to the list of primes. Repeat
            if(l==len(primes) and temp > 1):
                addPrime()
        i+=1

    #binomialProducts repeat from first half, so double
    for key in factors:
        factors[key]=factors[key]*2

    #if n is odd, there will be an odd number of terms.
    #Thus, we have to make one more pass through
    if n%2==0:
        # print(i+1)
        nextBinomial = nextBinomial * (n-i+1) // (i)
        # print(nextBinomial)
        temp = nextBinomial
        l = 0
        while(temp > 1):
            if temp%primes[l]==0:
                if not primes[l] in factors:
                    factors[primes[l]] = 0
                factors[primes[l]]+=1
                temp=temp//primes[l]
                l-=1
            l+=1
            if(l==len(primes) and temp > 1):
                addPrime()
                # print(primes)
    end = time.time()
    # print("Factors: " + str(end-start))
    # print("found all factors")
    # print(factors)
    sum = 1
    keys = list(factors.keys())
    start = time.time()
    for key in keys:
        tmpSum = ((key**(1+factors[key])-1)//(key-1))%1000000007
        # for exp in range(1,factors[key]+1):
        #     tmpSum += key**exp
        #     tmpSum=tmpSum%1000000007
        if tmpSum == 0:
            return 0
        sum*=tmpSum
        sum=sum%1000000007
    # print(sum)
    end = time.time()
    # print("Sum: " + str(end-start))
    return sum

def E(n,k,p):
    r=0
    e=0
    r=0
    if(k>n/2):
        k=n-k
    if(p>n-k):
        return (1)
    if(p>n/2):
        return (0)
    f=math.sqrt(n)
    if(p>f):
        if(n%p < k%p):
            return(1)
        else:
            return(0)
    while(n>0):
        a=n%p
        n=n//p
        b=k%p+r
        k=k//p
        if(a<b):
            e=e+1
            r=1
        else:
            r=0
    return(e)

def V9(n):
    global primes
    n=int(n)
    if(n<2):
        return 1
    factors = {}
    start = time.time()
    # find the factors
    for r in range(1,n):
        index = 0
        while(primes[index]<=n):
            t = E(n,r,primes[index])
            if t>0:
                if primes[index] not in factors:
                    factors[primes[index]]=0
                factors[primes[index]]+=t
                # print(t)
            index+=1
    end = time.time()
    # print("Factors: " + str(end-start))
    # print("found all factors")
    # print(factors)
    sum = 1
    keys = list(factors.keys())
    start = time.time()
    for key in keys:
        tmpSum = ((key**(1+factors[key])-1)//(key-1))%1000000007
        if tmpSum == 0:
            return 0
        sum*=tmpSum
        sum=sum%1000000007
    # print(sum)
    end = time.time()
    # print("Sum: " + str(end-start))
    return sum

def Legende(n,r,p):
    exp = 1
    count = 0
    # str(n-int(n)).split('.')[1]
    while((str(n/(p**exp)-n//(p**exp)).split('.')[1])<(str(r/(p**exp)-r//(p**exp)).split('.')[1])):
        count+=n//(p**exp)
        exp+=1
    return count

def V10(n):
    global primes
    n=int(n)
    if(n<2):
        return 1
    factors = {}
    start = time.time()
    # find the factors
    for r in range(1,int(n/2+1)):
        index = 0
        while(primes[index]<=n):
            # t1 = Legende(n,primes[index])
            # t2 = Legende(r,primes[index])
            # t3 = Legende(n-r,primes[index])
            # tSum = t1-t2-t3
            tSum=Legende(n,r,primes[index])
            if(tSum>0):
                if(primes[index] not in factors):
                    factors[primes[index]]=0
                factors[primes[index]]+=tSum
            index+=1
    for key in factors:
        factors[key]=factors[key]*2
    if n%2==0:
        index = 0
        r = int(n/2+1)
        while(primes[index]<=n):
            # t1 = Legende(n,primes[index])
            # t2 = Legende(r,primes[index])
            # t3 = Legende(n-r,primes[index])
            # tSum = t1-t2-t3
            tSum=Legende(n,r,primes[index])
            if(tSum>0):
                if(primes[index] not in factors):
                    factors[primes[index]]=0
                factors[primes[index]]+=tSum
            index+=1
    end = time.time()
    # print("Factors: " + str(end-start))
    # print("found all factors")
    # print(factors)
    sum = 1
    keys = list(factors.keys())
    start = time.time()
    for key in keys:
        tmpSum = ((key**(1+factors[key])-1)//(key-1))%1000000007
        if tmpSum == 0:
            return 0
        sum*=tmpSum
        sum=sum%1000000007
    # print(sum)
    end = time.time()
    # print("Sum: " + str(end-start))
    return sum

"""
Using Lucas' and Fermat's little theorem to calculate nCk mod m, m is prime
"""
# modular exponentiation: b^e % mod
def mod_exp(b,e,mod):
    r = 1
    while e > 0:
        if (e&1) == 1:
            r = (r*b)%mod
        b = (b*b)%mod
        e >>= 1

    return r

# get degree of p in n! (exponent of p in the factorization of n!)
def fact_exp(n,p):
    e = 0
    u = p
    t = n
    while u <= t:
        e += t//u
        u *= p
    return e

# convert given number n into array of its base b representation
# most significant digit is at rightmost position in array
def get_base_digits(n,b):
    d = []
    while n > 0:
        d.append(n % b)
        n  = n // b
    return d

# Using Fermat's little theorem to compute nCk mod p
# considering cancelation of p in numerator and denominator
# Note: p must be prime
def fermat_binom_advanced(n,k,p):
    # check if degrees work out
    num_degree = fact_exp(n,p) - fact_exp(n-k,p)
    den_degree = fact_exp(k,p)
    if num_degree > den_degree:
        return 0

    if k > n:
        return 0
    cur = 1
    # calculate numerator and cancel out occurrences of p
    num = 1
    for i in range(n,n-k,-1):
        cur = i
        while cur%p == 0:
            cur //= p
        num = (num*cur)%p
    cur=1
    # calculate denominator and cancel out occurrences of p
    denom = 1
    for i in range(1,k+1):
        cur = i
        while cur%p == 0:
            cur //= p
    denom = (denom*cur)%p

    # numerator * denominator^(p-2) (mod p)
    return (num * mod_exp(denom,p-2,p))%p

# Using Lucas' theorem to split the problem into smaller sub-problems
# In this version assuming p is prime
def lucas_binom(n,k,p):
    # get n and k in base p representation
    np = get_base_digits(n,p)
    kp = get_base_digits(k,p)

    # calculate (nCk) = (n0 choose k0)*(n1 choose k1) ... (ni choose ki) (mod p)
    binom = 1
    for i in range(len(np)-1,-1,-1):
        ni = np[i]
        ki = 0
        if i < len(kp):
            ki = kp[i]
        binom = (binom * fermat_binom_advanced(ni,ki,p)) % p
        if(binom==0):
            return 0
    return binom

def add_2_bases(n,r,p):
    n1 = get_base_digits(r,p)
    n2 = get_base_digits(n-r,p)
    count= 0
    i1 = len(n1)
    i2 = len(n2)
    carry = 0
    while i1>0 and i2>0:
        i1-=1
        i2-=1
        tmp = n1[i1]+n2[i2]+carry
        carry = tmp%p
        if(carry>0):
            return carry

def V11(n):
    global primes
    n=int(n)
    if(n<2):
        return 1
    factors = {}
    start = time.time()
    # find the factors
    t = int(n/2+1)
    if n%2 == 0:
        t = int(n/2)
    # int nextBinomial = 0
    for r in range(1,t):
        index = 0
        # nextBinomial = nextBinomial * (n-r+1) // (r)
        while(primes[index]<=n):
            tSum=lucas_binom(n,r,primes[index])
            if(tSum==0):
                # print("One factor is : " + str(primes[index]))
                if(primes[index] not in factors):
                    factors[primes[index]]=0
                t1 = fact_exp(n,primes[index])
                t2 = fact_exp(r,primes[index])
                t3 = fact_exp(n-r,primes[index])
                factors[primes[index]] += (t1-t2-t3)
                # factors[primes[index]]+=1#fact_exp(prime[index])
                # print("# of factors"+  str(fact_exp(n,primes[index])))
                # factors[primes[index]]+=Legende(n,r,primes[index])
            index+=1
    for key in factors:
        factors[key]=factors[key]*2
    # print('multiplied')
    if n%2==0:
        index = 0
        r = int(n/2)
        while(primes[index]<=n):
            # t1 = Legende(n,primes[index])
            # t2 = Legende(r,primes[index])
            # t3 = Legende(n-r,primes[index])
            # tSum = t1-t2-t3
            tSum=lucas_binom(n,r,primes[index])
            if(tSum==0):
                # print("One factor is : " + str(primes[index]))
                if(primes[index] not in factors):
                    factors[primes[index]]=0
                t1 = fact_exp(n,primes[index])
                t2 = fact_exp(r,primes[index])
                t3 = fact_exp(n-r,primes[index])
                factors[primes[index]] += (t1-t2-t3)
                # factors[primes[index]]+=1
            index+=1
    end = time.time()
    # print("Factors: " + str(end-start))
    # print("found all factors")
    # print(factors)
    sum = 1
    keys = list(factors.keys())
    start = time.time()
    for key in keys:
        tmpSum = ((key**(1+factors[key])-1)//(key-1))%1000000007
        if tmpSum == 0:
            return 0
        sum*=tmpSum
        sum=sum%1000000007
    # print(sum)
    end = time.time()
    # print("Sum: " + str(end-start))
    return sum

spf=[0,1]

def seive(n):
    global spf
    spf+=[0]*n
    #set each number to itself
    for i in range(n):
        spf[i]=i
    # starting at 2, see if the number is prime/hasn't been changed
    # then mark every number that is divisible by that number
    # this method gets the smallest prime factor of a number.
    for i in range(2,n):
        if(i==spf[i]):
            for j in range(i*i,n,i):
                if(spf[j]==j):
                    spf[j]=i

#good idea, too much space
def V12(n):
    global spf
    n=int(n)
    if(n<2):
        return 1
    factors = {}
    start = time.time()
    # find the factors
    i = 1
    start = time.time()
    nextBinomial =1
    while i <= int((n-1)/2):
        # print(i+1)
        nextBinomial = nextBinomial * (n-i+1) // (i)
        tmp = nextBinomial
        while tmp!=1:
            prime = spf[tmp]
            if(not prime in factors):
                factors[prime]=0
            factors[prime]+=1
            tmp=tmp//prime
        i+=1
    for key in factors:
        factors[key]=factors[key]*2
    if n%2==0:
        nextBinomial = nextBinomial * (n-i+1) // (i)
        tmp = nextBinomial
        while tmp!=1:
            prime = spf[tmp]
            if(not prime in factors):
                factors[prime]=0
            factors[prime]+=1
            tmp=tmp//prime
    end = time.time()
    sum = 1
    keys = list(factors.keys())
    start = time.time()
    for key in keys:
        tmpSum = ((key**(1+factors[key])-1)//(key-1))%1000000007
        if tmpSum == 0:
            return 0
        sum*=tmpSum
        sum=sum%1000000007
    # print(sum)
    end = time.time()
    # print("Sum: " + str(end-start))
    return sum

#Fermat's algorith
#any n = a*a-b*b , where n is odd
# shuffled, it's b*b = a*a-n
def fermat(n):
    a = int(1+math.sqrt(n))
    BB = n-a*a
    while(int(math.sqrt(BB)) != math.sqrt(BB)):
        a+=1
    return a

def V13(n):
    global primes
    n=int(n)
    if(n<2):
        return 1
    factors = {}
    nextBinomial = 1
    i = 1
    start = time.time()
    while i <= int((n-1)/2):
        # print(i+1)
        nextBinomial = nextBinomial * (n-i+1) // (i)
        # print(nextBinomial)
        temp = nextBinomial
        l = 0
        while(temp > 1):
            if temp%primes[l]==0:
                if not primes[l] in factors:
                    factors[primes[l]] = 0
                factors[primes[l]]+=1
                temp=temp//primes[l]
                l-=1
            l+=1
            if(l==len(primes) and temp > 1):
                addPrime()
                # print(primes)
        i+=1
    for key in factors:
        factors[key]=factors[key]*2
    if n%2==0:
        # print(i+1)
        nextBinomial = nextBinomial * (n-i+1) // (i)
        # print(nextBinomial)
        temp = nextBinomial
        l = 0
        while(temp > 1):
            if temp%primes[l]==0:
                if not primes[l] in factors:
                    factors[primes[l]] = 0
                factors[primes[l]]+=1
                temp=temp//primes[l]
                l-=1
            l+=1
            if(l==len(primes) and temp > 1):
                addPrime()
                # print(primes)
    end = time.time()
    # print("Factors: " + str(end-start))
    # print("found all factors")
    # print(factors)
    sum = 1
    keys = list(factors.keys())
    start = time.time()
    for key in keys:
        tmpSum = ((key**(1+factors[key])-1)//(key-1))%1000000007
        # for exp in range(1,factors[key]+1):
        #     tmpSum += key**exp
        #     tmpSum=tmpSum%1000000007
        if tmpSum == 0:
            return 0
        sum*=tmpSum
        sum=sum%1000000007
    # print(sum)
    end = time.time()
    # print("Sum: " + str(end-start))
    return sum

def addPrimesInFile():
    global primes
    f = open("C:/Users/Admin/Documents/Coding/Python/PE/Primes.txt", "r")
    # work_data = f.readlines
    for line in f:
        words = line.split();
        for word in words:
            primes+=[int(word)]

def main():
    sum = 0
    current = 0
    x = int(input("How high?"))
    f = open("C:/Users/Admin/Documents/Coding/Python/PE/P650Nums.txt", "r")
    work_data = f.readlines()
    while current<x and current<len(work_data):
        sum=int(work_data[current])
        # print(work_data[current])
        current+=1
    # current+=1
    # PrimesTo20000()
    addPrimesInFile()
    f = open("C:/Users/Admin/Documents/Coding/Python/PE/P650Nums.txt", "a")
    # print(int(V7(x)))
    # V6: 0.2798879146575928
    # V7: 32.21831011772156
    # V7(improved): 29.772693395614624
    # seive(50000000)
    input("Continue?")
    start = time.time()
    for i in range(current+1,int(x)+1):
        print(i)
        t = int(V8(i))%1000000007
        sum+=t
        sum=sum%1000000007
        f.write(str(sum)+ "\n")
        # print(t)
    print()
    print(sum)
    end = time.time()
    print("This operation took " + str(end-start) + " seconds")
    # print(S(int(x)))
    # print(S(20000))

if __name__ == '__main__':
    main()
