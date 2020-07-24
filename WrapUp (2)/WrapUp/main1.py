"""
Wrap-Up 1
Morgan Johnstone

Task C:
    -User Specified path of ASCII grid files
    -Check if both are the same size (rows and cols)
    -Ask user which operation to perform
        -Sum, Difference, Multiplication, Division
    -Performs cell by cell alg
    -Saves new file back to ASCII grid file
"""
import csv
import numpy as np

def sumIt(a,b):
    '''
    Will sum each cell of both ascii
    and return a new summed file.
    '''
    return 0

def diffIt(a,b):
    '''
    Will subtract each cell of each ascii
    and return a new diff'ed file.
    '''
    return 0

def proIt(a,b):
    '''
    Will multiply each cell of each ascii
    and return a new multiplied file.
    '''
    return 0

def quoIt(a,b):
    '''
    Will divide each cell of each ascii
    and return a new divided file.
    '''

    return 0


def theBeginning():
    asciiOne = r"C:\Users\mogaj\Desktop\WrapUp\datasets\TaskC\rasterA.txt"
    asciiTwo = r"C:\Users\mogaj\Desktop\WrapUp\datasets\TaskC\rasterB.txt"
    asciiOut = r""

    opers = {"s":sumIt, "d":diffIt, "p":proIt, "q":quoIt}

    success = False
    while not success:
        if asciiOne == 0 or asciiTwo == 0:
            asciiOne = input("Please enter the 1st file path: ")
            asciiTwo = input("Please enter the 2nd file path: ")
        try:
            with open(r"{}".format(asciiOne),"r") as f1, open(r"{}".format(asciiTwo), "r") as f2:
                print("hello")
                success = True
                a1 = np.empty()
                a2 = np.empty()
                for x,y in f1,f2:
                    arraya = arrayb = []
                    for i,j in x,y:
                        arraya.append(i)
                        arrayb.append(j)
                    a1.append(arraya)
                    a2.append(arrayb)
                print("lenf1")
                if count1 == count2:
                    print("lenf1[0]")
                    option = input("Please enter preferred operation: sum (s), difference (d), product (p), quotient (q).  ")
                    newFile = opers[option.lower().strip()](f1,f2)
                    with open(asciiOut,"w") as out:
                        for line in newFile:
                            out.write(line)
                        out.close()


        except:
            print("One provided file path does not exist. Please try again. ")
            asciiOne = 0
            asciiTwo = 0

theBeginning()
