# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

#param s string to remove index from
#param i index to remove
def delIndexFromString(s,i):
    s = s[:i] + s[i+1:]
    return s

#param n1 first to get digits of
#param n2 comparing if has same digits as n1
def compareNumbers(n1,n2):
    if(not len(n1) == len(n2)):
        return False
    kIndex1 = 0
    while(kIndex1<len(n1)):
        kIndex2 = 0
        found = False
        while(kIndex2<len(n2) and not found):
            if(n1[kIndex1] == n2[kIndex2]):
                found = True
                delIndexFromString(n1,kIndex1)
                delIndexFromString(n2,kIndex2)
            kIndex2+=1
        kIndex1+=1
        if(not found):
            return False
    return True

def main():
    kInt = 1
    while(True):
        kScalar = 2
        works = True
        while(kScalar < 7 and works):
            works = compareNumbers(str(kInt), str(kInt*kScalar))
            kScalar+=1
        if(works):
            print(kInt)
            return
        kInt+=1

if __name__ == '__main__':
    main()
