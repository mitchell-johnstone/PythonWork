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

asciiOne = r"C:\Users\mogaj\Desktop\WrapUp\datasets\TaskC\rasterA.txt"
asciiTwo = r"C:\Users\mogaj\Desktop\WrapUp\datasets\TaskC\rasterB.txt"
asciiOut = r"C:\Users\mogaj\Desktop\WrapUp\datasets\TaskC\rasterC.txt"

def sumIt(a,b):
    '''
    Will sum each cell of both ascii
    and return a new summed file.
    '''
    newArray = a
    for i in range(len(a)):
        for j in range(len(a[0])):
            newArray[i][j] = a[i][j]+b[i][j]
    return newArray

def diffIt(a,b):
    '''
    Will subtract each cell of each ascii
    and return a new diff'ed file.
    '''
    newArray = a
    for i in range(len(a)):
        for j in range(len(a[0])):
            newArray[i][j] = a[i][j]-b[i][j]
    return newArray


def proIt(a,b):
    '''
    Will multiply each cell of each ascii
    and return a new multiplied file.
    '''
    newArray = a
    for i in range(len(a)):
        for j in range(len(a[0])):
            newArray[i][j] = a[i][j]*b[i][j]
    return newArray

def quoIt(a,b):
    '''
    Will divide each cell of each ascii
    and return a new divided file.
    '''
    newArray = a
    for i in range(len(a)):
        for j in range(len(a[0])):
            if b[i][j] == 0:
                newArray[i][j] = "noData"
            else:
                newArray[i][j] = a[i][j]/b[i][j]
    return newArray

def theBeginning(asciiOne,asciiTwo,asciiOut):
    #Opers dictionary holds all the function calls for later
    opers = {'1':sumIt, '2':diffIt, '3':proIt, '4':quoIt}
    success = False
    while not success:
        if asciiOne == 0 or asciiTwo == 0:
            asciiOne = input("Please enter the 1st file path: ")
            asciiTwo = input("Please enter the 2nd file path: ")
        try:
            newFile = []
            with open(r"{}".format(asciiOne),"r") as f1, open(r"{}".format(asciiTwo), "r") as f2:
                success = True
                arrays = [[],[]]
                files = [f1,f2]
                for x in range(len(arrays)): #uses the index of the array to index the files too
                    for row in files[x]: #for row in the specific file
                        newRow = row.strip("\r\n").split(" ") #removes the newline characters, and splits by spaces
                        for i in range(len(newRow)):
                            newRow[i]= int(newRow[i]) # reInputs the data as ints for the operations later
                        arrays[x].append(newRow)
                ##Optional Print Statements
                print("The given files are below: ")
                print("\nA")
                for elem in arrays[0]:
                    print(elem)
                print("\nB")
                for elem in arrays[1]:
                    print(elem)
                ##End of optional print statements
                if len(arrays[0])==len(arrays[1]):
                    if len(arrays[0][0]) == len(arrays[1][0]):
                        accurate = False
                        while not accurate:
                            optIt = input("\nPlease enter preferred operation: sum (1), difference (2), product (3), quotient (4). ")
                            if optIt in opers.keys():
                                accurate = True
                        newFile = opers[optIt](arrays[0],arrays[1]) #calls the various function from the dictionary it's stored in
                        ##Another optional print statement
                        print("\nThe new file is as follows: ")
                        print("\nNew")
                        for elem in newFile:
                            print(elem)
                        ##End of optional print statement
                else:
                    #Makes sure you can loop through again if something goes wrong
                    success = False
                f1.close()
                f2.close()
            with open(asciiOut,'w') as fileOut:
                writer = csv.writer(fileOut)
                for line in newFile:
                    writer.writerow(line)
                fileOut.close()
            print("\n... Completed")
        except:
            print("Something was wrong with one of the files provided. Please try again. ")
            asciiOne = 0
            asciiTwo = 0

theBeginning(asciiOne,asciiTwo,asciiOut)
