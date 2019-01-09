def main():
    highestVal = 0
    highestIndex = 0
    for den in range(1000):
        den+=1
        num = 1
        print()
        print(den)
        values = []
        r = 0
        while (num>0) & (num not in values):
            values = values + [num]
            while num<den:
                num = num * 10
            r = num//den
            num = num - den*r
        print(values)
        if (num in values):
            t = values.index(num)
            if((len(values)-t)>highestVal):
                highestVal = len(values)-t
                highestIndex = den;
    print()
    print("Highest Index:")
    print(highestIndex)
    print("Highest length:")
    print(highestVal)

if __name__ == '__main__':
    main()
