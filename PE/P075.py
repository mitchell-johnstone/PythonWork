import math
import numpy as np
def findTriangles(L):
    if L%2==1:
        return 0 #no odd perimeter right triangles
    else:
        pair = ()
        for b in range(1,L//2):
            a = L/2 * ((L-2*b)/(L-b))
            inta = int(a)
            if a == inta:
                if pair and pair != tuple(sorted((inta,b))):
                    return 0
                elif not pair:
                    pair = tuple(sorted((inta,b)))
        # print(L, " gives triangle ", pair)
        return 1 if pair else 0


def V1():
    print("Starting calculation...")
    triangleCount = 0
    for L in range(12,1500001):
        triangleCount += findTriangles(L)
    print("All Finished!")
    print(triangleCount)


def v2():
    #If we have that
    # a = m**2 - n**2
    # b = 2mn
    # c = m**2 + n**2
    # we can create different sides/perimeters since
    # p = 2m*(m+n)
    perimeters = []
    sides = [[]]
    total = 0
    for m in range(1,int((150000//2)**.5)):
        print("current M: ", m)
        #note n cannot be greater than m
        #else a would be negative
        for n in range(1, m):
            # c = m**2 + n**2
            p = 2*m*(m+n)
            #check if perimeter exceeds our range
            if p>1500000:
                break
            #check to see if we already have these sides listed for a perimeter
            a = m**2 - n**2
            b = 2*m*n
            currentSides = list(sorted([a,b]))
            if currentSides in sides:
                continue
            for k in range(1, 1500000//p):
                sides+= [x*k for x in currentSides]
                perimeters += [k*p]
    print("Finished calculating all possible perimeters under 1,500,000")
    #print(sides)
    for p in perimeters:
        count = 0
        while p in perimeters:
            count+=1
            perimeters.remove(p)
        if count == 1:
            total += 1
    print("total number of perimeters with one triangle: " , total)


def findTrianglesForLength(L):
    oneSolution = False
    for m in range(1, int((L/2)**.5)):
        n = (L - 2*(m**2))
        if n<m and n%(2*m)==0:
            if True:
                n//=2*m
                print("a=",m**2-n**2," b=",2*m*n," c=",m**2+n**2) 
            if oneSolution:
                return 0
            else:
                oneSolution = True
    return 1 if oneSolution else 0


def v3():
    print(sum(findTrianglesForLength(L) for L in range(12,1500000,2)))


#function to see if a and b make a right triangle
#returns value of c if it exists
def validC(a,b):
    c = (a**2 + b**2)**.5
    if int(c)/1.0 == c:
        return int(c)
    else: return 0


def v4():
    goodPerimeters, badPerimeters = [], []
    for a in range(1,1500000//2+1):
        print(a)
        for b in range(1,a):
            c = validC(a,b)
            if c:
                p = a + b + c
                if p>1500000:
                    break
                elif p in badPerimeters:
                    continue
                elif p in goodPerimeters:
                    goodPerimeters.remove(p)
                    badPerimeters.append(p)
                else:
                    goodPerimeters.append(p)
    print(len(goodPerimeters))


def v5():
    #If we have that
    # a = m**2 - n**2
    # b = 2mn
    # c = m**2 + n**2
    # we can create different sides/perimeters since
    # p = 2m*(m+n)
    goodPerimeters, badPerimeters = [], []
    print("Beginning...")
    for m in range(2,int((150000//2)**.5)+1):
        print("current M: ", m)
        odd = m%2
        #note n cannot be greater than m
        #else a would be negative
        for n in range(1, m):
            #make sure that m and n are coprime for euclid equation to work
            #also must not both be odd
            if (odd and n%2) or math.gcd(m,n) != 1: continue
            tp = 2*m*(m+n)
            #check if perimeter exceeds our range
            #if so, then no further n will be under our range for given m
            if tp>1500000:
                break
            #a = m**2 - n**2
            #b = 2*m*n
            #c = m**2 + n**2
            for k in range(1, 1500000//tp+1):
                p = k*tp
                if p>1500000:
                    break
                elif p in badPerimeters:
                    continue
                elif p in goodPerimeters:
                    goodPerimeters.remove(p)
                    badPerimeters.append(p)
                else:
                    goodPerimeters.append(p)
    print(len(goodPerimeters))


def generateTree(startingVector,aMatrix,bMatrix,cMatrix,maxPerimeter,
                 goodPerimeters,badPerimeters):
    currentPerimeter = np.sum(startingVector)
    if currentPerimeter > maxPerimeter: return
    print(startingVector)
    for k in range(1, maxPerimeter//currentPerimeter+1):
        p = k*currentPerimeter
        if p>maxPerimeter:
            break
        elif p in badPerimeters:
            continue
        elif p in goodPerimeters:
            goodPerimeters.remove(p)
            badPerimeters.append(p)
        else:
            goodPerimeters.append(p)
    generateTree(aMatrix.dot(startingVector),aMatrix,bMatrix,cMatrix,
                 maxPerimeter,goodPerimeters,badPerimeters)
    generateTree(bMatrix.dot(startingVector),aMatrix,bMatrix,cMatrix,
                 maxPerimeter,goodPerimeters,badPerimeters)
    generateTree(cMatrix.dot(startingVector),aMatrix,bMatrix,cMatrix,
                 maxPerimeter,goodPerimeters,badPerimeters)


def v6():
    aMatrix = np.array([[1,-2,2],
                        [2,-1,2],
                        [2,-2,3]])
    bMatrix = np.array([[1,2,2],
                        [2,1,2],
                        [2,2,3]])
    cMatrix = np.array([[-1,2,2],
                        [-2,1,2],
                        [-2,2,3]])
    startingVector = np.array([3,4,5])
    goodPerimeters, badPerimeters = [], []
    generateTree(startingVector,aMatrix,bMatrix,cMatrix,1500000,
                 goodPerimeters,badPerimeters)
    print(goodPerimeters)
    print(len(goodPerimeters))


def generateTree2(startingVector,aMatrix,bMatrix,cMatrix,maxPerimeter,
                  perimeters):
    currentPerimeter = np.sum(startingVector)
    if currentPerimeter > maxPerimeter: return
    #print(startingVector)
    for k in range(1, maxPerimeter//currentPerimeter+1):
        perimeters[k*currentPerimeter] += 1
    generateTree2(aMatrix.dot(startingVector),aMatrix,bMatrix,cMatrix,
                  maxPerimeter,perimeters)
    generateTree2(bMatrix.dot(startingVector),aMatrix,bMatrix,cMatrix,
                  maxPerimeter,perimeters)
    generateTree2(cMatrix.dot(startingVector),aMatrix,bMatrix,cMatrix,
                  maxPerimeter,perimeters)

def v7():
    aMatrix = np.array([[1,-2,2],
                        [2,-1,2],
                        [2,-2,3]])
    bMatrix = np.array([[1,2,2],
                        [2,1,2],
                        [2,2,3]])
    cMatrix = np.array([[-1,2,2],
                        [-2,1,2],
                        [-2,2,3]])
    startingVector = np.array([3,4,5])
    perimeters = [0] * 1500001
    generateTree2(startingVector,aMatrix,bMatrix,cMatrix,1500000,perimeters)
    print(sum([p for p in perimeters if p==1]))


def main():
    v7()
    return
    #v3()
    print(findTriangles(120))
    print(findTrianglesForLength(120))

if __name__ == "__main__":
    main()
