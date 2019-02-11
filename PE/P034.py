# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

def factorial(i):
    if(i==0): return 1
    return i*factorial(i-1)


def main():
    factorials = [0]*10
    for i in range(10):
        factorials[i] = factorial(i)
        print(factorials[i])
    bigSum = 0
    for i in range(10,999999):
        originalNumber = i
        possibleSum = 0
        i=str(i)
        for char in i:
            possibleSum+=factorials[int(char)]
        if(possibleSum==originalNumber):
            bigSum+=originalNumber
            print(originalNumber)
    print(bigSum)

if __name__ == "__main__":
    main()