# There are exactly ten ways of selecting three from five, 12345:
#
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#
# In combinatorics, we use the notation, 5C3=10.
#
# In general, nCr=n!r!(n−r)!, where r≤n, n!=n×(n−1)×...×3×2×1, and 0!=1.
#
# It is not until n=23, that a value exceeds one-million: 23C10=1144066.
#
# How many, not necessarily distinct, values of nCr for 1≤n≤100, are greater than one-million?

def main():
    COUNT = 0
    n = 2
    while(n <= 100):
        r = 1
        nextBinomial = 1
        middle = ( (n-1) // 2)
        while(r <= middle ):
            nextBinomial = nextBinomial * (n-r+1) // (r)
            if(nextBinomial>10**6):
                COUNT+=2*(middle - r + 1)
                r = middle
                print(n,"C",r,"=",nextBinomial)
                # return
            r+=1
        if(n%2 == 0):
            nextBinomial = nextBinomial * (n-r+1) // (r)
            if(nextBinomial>10**6):
                COUNT+=1
        n+=1
    print(COUNT)
    return

if __name__ == '__main__':
    main()
