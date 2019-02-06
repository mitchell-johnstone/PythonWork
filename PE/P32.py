# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
import time

def nextLexographic(n):
    firstIndex = len(n)-2
    while(firstIndex>=0):
        if n[firstIndex]<n[firstIndex+1]:
            break
        firstIndex-=1
    secondIndex = firstIndex+1
    tmpIndex = secondIndex
    while(tmpIndex<len(n)):
        if(n[tmpIndex]>n[firstIndex] and n[tmpIndex]<n[secondIndex]):
            secondIndex=tmpIndex
        tmpIndex+=1
    tmp = n[firstIndex]
    # n[firstIndex]=n[secondIndex]
    n=n[0:firstIndex]+n[secondIndex]+ n[firstIndex+1:]
    # n[secondIndex] = tmp
    n=n[0:secondIndex]+tmp+n[secondIndex+1:]
    firstIndex+=1
    while(firstIndex<len(n)-1):
        secondIndex=firstIndex+1
        while(secondIndex<len(n)):
            if n[firstIndex]>n[secondIndex]:
                tmp=n[firstIndex]
                # n[firstIndex]=n[secondIndex]
                n=n[0:firstIndex]+n[secondIndex]+ n[firstIndex+1:]
                # n[secondIndex] = tmp
                n=n[0:secondIndex]+tmp+n[secondIndex+1:]
            secondIndex+=1
        firstIndex+=1
    return n

def OneXFour(n):
    num1 = int(n[0])
    num2 = int(n[1:5])
    product = int(n[5:])
    if((num1*num2)==product):
        print(str(num1)+ " * " + str(num2) +  " = " + str(product))
        return product
    return 1

def TwoXThree(n):
    num1 = int(n[0:2])
    num2 = int(n[2:5])
    product = int(n[5:])
    if((num1*num2)==product):
        print(str(num1)+ " * " + str(num2) +  " = " + str(product))
        return product
    return 1

def V1():
    numbers = "123456789"
    count=[]
    while(not numbers=="987654321"):
    # for i in range(10):
        numbers = nextLexographic(numbers)
        tmp=(OneXFour(numbers))
        if(tmp not in count):
            count+=[tmp]
        tmp=(TwoXThree(numbers))
        if(tmp not in count):
            count+=[tmp]
        # print(numbers)
    print(count)
    return sum(count)-1

def main():
    print("Starting...")
    start = time.time()
    print(V1())
    end = time.time()
    print("this operation took:" + str(end-start)+ " seconds")


if __name__ == '__main__':
    main()
