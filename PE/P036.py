# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)

# method to convert decimal to binary
def toBinary(n):
    return int(bin(n)[2:])

# method to check if number is palindromic
def isPalindrome(n):
    #convert n to str to reverse easier
    n = str(n)
    #make a reversed copy
    RN = n[::-1]
    #see if reversed and normal are the same
    return n == RN

def main():
    palindromicSum = 0
    #I split the if statements to reduce time and computation
    for current in range(1000000):
        #check if the current number is a palidrome
        if(isPalindrome(current)):
            #next check if the binary version of the number is a palindrome
            binary = toBinary(current)
            if(isPalindrome(binary)):
                #if both are true, add one to the counter
                palindromicSum+=current
                print(current," ",binary)
    print("\n",palindromicSum)

if __name__ == '__main__':
    main()
