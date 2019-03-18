# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
def factorsMatchTarget(cur, tar):
    
    #value to keep the current divisor
    divisor = 3

    #var to hold the number of factors
    numOfFactors = 0

    #loop and divide by 2, that way we only have to divide by odd numbers
    while(cur%2==0):
        cur = cur//2
        numOfFactors=1

    while cur>1:
        #bool to see if the divisor really divides into cur
        divided = False

        #loop until the current number is not divisible by divisor
        while (cur%divisor==0):
            cur//=divisor
            divided = True

        divisor+=2

        #if the divisor is a proper factor, add one to num of factors
        if(divided):
            numOfFactors+=1
        if(numOfFactors>tar):
            return False

    return numOfFactors == tar

def main():
    #target for # of terms needed and # of factors
    target = int(input("What is the target?"))

    #values to hold the current terms
    values = [1]
    for i in range(target-1):
        values+=[i+2]

    #repeat until answer is found
    while(True):

        #var to hold how much to shift each time
        shiftAmt = 0

        #find how much we need to shift by
        for i in range(len(values)):
            if not factorsMatchTarget(values[i],target):
                shiftAmt = i+1

        #if we don't shift, that means we have the correct numbers
        if(shiftAmt==0):
            print(values)
            print(sum(values))
            return

        #shift by the shift amount
        for i in range(len(values)):
            values[i] += shiftAmt
        # print(values)

if __name__ == '__main__':
    main()
