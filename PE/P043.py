# The number, 1406357289, is a 0 to 9 pandigital number because
# it is made up of each of the digits 0 to 9 in some order,
# but it also has a rather interesting sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on.
# In this way, we note the following:
#
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
#
# Find the sum of all 0 to 9 pandigital numbers with this property.

# pandigital in reverse order
def backwardPandigital(n):
    #set n to str
    n = (str(n))

    #find first occurence that an index is lower than the one to the left of it
    firstNum = len(n)-1
    while(firstNum>=0):
        firstNum-=1
        if(n[firstNum] > n[firstNum+1]):
            break

    #find num directly below n[firstNum]
    secondNum = firstNum+1
    t = secondNum
    while(t<len(n)):
      # print("checking for 2nd")
      if(n[t] < n[firstNum] and n[t]>n[secondNum]):
        secondNum = t
      t+=1

    #switch first and second
    n = n[:firstNum] + n[secondNum] + n[firstNum+1:secondNum] + n[firstNum] + n[secondNum+1:]

    #reset the rest of the string to go in descending order
    for i in range(firstNum+1,len(n)-1):
        # print("Reversing")
        for j in range(i+1,len(n)):
            if n[i]<n[j]:
                n = n[:i] + n[j] + n[i+1:j] + n[i] + n[j+1:]

    return int(n)

#pandigital rising
def forwardPandigital(n):
    #set n to str
    n = (str(n))

    #find first occurence that an index is lower than the one to the left of it
    firstNum = len(n)-1
    while(firstNum>=0):
        firstNum-=1
        if(n[firstNum] < n[firstNum+1]):
            break

    #find num directly below n[firstNum]
    secondNum = firstNum+1
    t = secondNum
    while(t<len(n)):
      # print("checking for 2nd")
      if(n[t] > n[firstNum] and n[t]<n[secondNum]):
        secondNum = t
      t+=1

    #switch first and second
    n = n[:firstNum] + n[secondNum] + n[firstNum+1:secondNum] + n[firstNum] + n[secondNum+1:]

    #reset the rest of the string to go in descending order
    for i in range(firstNum+1,len(n)-1):
        # print("Reversing")
        for j in range(i+1,len(n)):
            if n[i]>n[j]:
                n = n[:i] + n[j] + n[i+1:j] + n[i] + n[j+1:]

    return int(n)

def partDivisibleByX(n,start,end,x):
    n=str(n)
    tmp = int(n[start:end])
    return tmp%x==0

def main():
    sum = 0
    cur = 9876543210
    divisors = [2,3,5,7,11,13,17]
    while(cur>1023456789):
        divisible = True
        for i in range(len(divisors)):
            if not partDivisibleByX(cur,i+1,i+4,divisors[i]):
                divisible = False
        if(divisible):
            sum+=cur
            print(cur)
        cur = backwardPandigital(cur)
    print("\n",sum)

if __name__ == '__main__':
    main()
