# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

def main():
    #how high to go to
    target = int(input("How hight? "))

    #var to hold the answer
    tenDigits = 0

    #python is really good at holding big numbers,
    #so we only have to loop to the target and add the digits
    for curNum in range(1,target+1):
        tenDigits+=(curNum**curNum)%10000000000

        #get the remainder to get the last 10 digits
        tenDigits = tenDigits% 10000000000
        
    print(tenDigits)

if __name__ == '__main__':
    main()
