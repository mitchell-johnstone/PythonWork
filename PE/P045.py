# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
#
# Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
# Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.
#
# Find the next triangle number that is also pentagonal and hexagonal.

#H will always be the lowest value
def H(n):
    return n*(2*n-1)

#P is middle
def P(n):
    return n*(3*n-1)//2

#T is highest
def T(n):
    return n*(n+1)//2

#H should be calculated first
#Then go up in P until P is over H
#fianlly, if they are the same, do the same with T
def main():
    #declaring index variables for H, P, and T
    curH,curP,curT=144,2,2

    #val for H
    hVal = 0

    #repeat forever, adding 1 to H everytime
    while(True):
        curH+=1
        hVal = H(curH)

        #continuously add to curP until p(curP+1) > H(CurH)
        while(P(curP+1)<=hVal):
            curP+=1

        #do the same for T
        while(T(curT+1)<=hVal):
            curT+=1

        # print(hVal,P(curP),T(curT))

        if(hVal == P(curP) and hVal == T(curT)):
            print(T(curT))
            return

if __name__ == '__main__':
    main()
