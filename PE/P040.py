# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

def main():
    #var for result
    result = 1
    # var to hold the next target digit
    targetDigit = 1
    #var to hold current digit
    currentD = 0
    #var to hold the current positive int
    currentI = 0
    while(targetDigit<=1000000):
        #increment current int and update digit count
        currentI+=1
        tmp = str(currentI)
        currentD+=len(tmp)

        #check if at the target digit
        if(currentD==targetDigit):
            result*=int(tmp[len(tmp)-1])
            targetDigit*=10
        #check if gone past the target
        elif(currentD>targetDigit):
            result*=int(tmp[len(tmp)-currentD+targetDigit-1])
            targetDigit*=10
    print(result)

if __name__ == '__main__':
    main()
