# Take the number 192 and multiply it by each of 1, 2, and 3:
#
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

#nice direct approach, takes way too long
def nextPandigital(n):
    #variable to tell whether to return number
    c = False
    while(not c):
        c = True
        #empty set of booleans
        bools = [False]*9
        n-=1
        print(n)
        tmp = str(n)
        # load in array
        # if a number is present, set their index as True
        for i in range(9):
            bools[int(tmp[i])-1] = True
        # run through bools, and see if there is a false somewhere
        for bool in bools:
            if not bool:
                c = False
    return n

#anti-lexigraphic ordering :)
def antiPandigitalV2(n):
    #set n to str
    n = (str(n))

    #find first occurence that an index is lower than the one to the left of it
    firstNum = 8
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
    for i in range(firstNum+1,8):
        # print("Reversing")
        for j in range(i+1,9):
            if n[i]<n[j]:
                n = n[:i] + n[j] + n[i+1:j] + n[i] + n[j+1:]

    return int(n)

def isConcatenated(n):
    #convert the in to str
    n = str(n)


    baseNumber = 0

    # get what the base number will be
    # at max, the first number must be 4 digits
    for baseDigits in range(4):
        # test string to compare to n
        test = ""

        # baseNumber to be multiplied to get the rest of concatenated
        baseNumber = int(n[:baseDigits+1])

        #multiplier to multiply baseNumber
        multiplier = 1

        #loop unit the word is at or over 9 characters
        while(len(test)<9):
            test+=str(baseNumber*multiplier)
            multiplier+=1
        # print(test)
        if(test == n):
            return True
    return False

def main():
    #variable to hold current number
    currentNum = 987654321

    #this is a known concatenated variable, check to see if it returns true
    print(isConcatenated(192384576))

    #loop unit we get a concatenated string
    while(not isConcatenated(currentNum)):
        currentNum = antiPandigitalV2(currentNum)
        print(currentNum)
    #print result
    print(currentNum)

if __name__ == '__main__':
    main()
