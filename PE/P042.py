# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
# so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
# If the word value is a triangle number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'),
# a 16K text file containing nearly two-thousand common English words,
# how many are triangle words?

#method to take a character and return its corresponding value
def getValOfChar(c):
    if c == "A":
        return 1
    if c == "B":
        return 2
    if c == "C":
        return 3
    if c == "D":
        return 4
    if c == "E":
        return 5
    if c == "F":
        return 6
    if c == "G":
        return 7
    if c == "H":
        return 8
    if c == "I":
        return 9
    if c == "J":
        return 10
    if c == "K":
        return 11
    if c == "L":
        return 12
    if c == "M":
        return 13
    if c == "N":
        return 14
    if c == "O":
        return 15
    if c == "P":
        return 16
    if c == "Q":
        return 17
    if c == "R":
        return 18
    if c == "S":
        return 19
    if c == "T":
        return 20
    if c == "U":
        return 21
    if c == "V":
        return 22
    if c == "W":
        return 23
    if c == "X":
        return 24
    if c == "Y":
        return 25
    if c == "Z":
        return 26
    else:
        return 0

#taking a word, returning back a sum of the value of its chars
def wordToVal(w):
    #sum holds sum of characters
    sum = 0

    #run through the chars in the word, add up parts
    for c in w:
        sum+=getValOfChar(c)

    return sum

#method to get words from the file
def getWords():
    #open the file
    f = open("C:\\Users\\Admin\\Documents\\Coding\\Python\\PE\\P042_words.txt", "r")

    #read the words into a var
    allWords = f.read()

    #split the string of words into an array Of Words
    arrayOfWords = allWords.split("\",\"")
    return arrayOfWords

#method to get the nth term of triangle numbers
def triangleNumber(n):
    return n*(n+1)//2

def main():
    count = 0

    #array to hold all arrays
    words = getWords()
    print(words)
    
    #go through every word, checking if word is a triangleNumber
    for word in words:
        val = wordToVal(word)
        i=0
        triangle = triangleNumber(i)
        while(triangle<val):
            i+=1
            triangle = triangleNumber(i)
        if(val == triangle):
            count += 1

    print(count)

if __name__ == '__main__':
    main()
