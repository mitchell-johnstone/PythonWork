import random
#used for all letters
def replaceLetters(phrase, phraseHidden, letter):
    tmp = ""
    for i in range(len(phrase)):
        if phraseHidden[i*2] != "_":
            tmp+=phraseHidden[i*2] + " "
        elif phrase[i] == letter:
            tmp += letter + " "
        elif phrase[i] == " ":
            tmp += "  "
        else:
            tmp += "_ "
    return tmp

#return winnings, correctly guessed or not
def solveThePuzzle(phrase, winnings):
    guess = input("What\'s your best guess (be sure to use single spaces!)?").upper()
    if guess == phrase:
        print("That\'s correct - you solved the puzzle!")
        return [0, True]
    else:
        print("Sorry, that guess is incorrect! Your winnings will start over at $0 :(")
        return [-1*winnings, False]

#return winnings, vowel guessed, and if guess was correct
def buyAVowel(phrase, winnings):
    vowels = ("A", "E","I","O","U",)
    end = False
    while(not end):
        guess = input("Which vowel would you like to buy (A,E,I,O,U,)?: ").upper()
        if(guess in vowels):
            end = True
        else:
            print("Sorry, that is not a vowel. Guess again.")
    count = 0
    for c in phrase:
        if c == guess:
            count +=1
    return [-250, guess, count]

#return winnings, consonant guessed, and if guess was correct
def spinTheWheel(phrase, winnings):
    vowels = ("A", "E","I","O","U"," ")
    values = [50,  100,  100,  100,  100,  100,  100,  200,  200,  200,  200, 250,  250,  250,  500,  500,  750,  750,  1000,  2000,  5000,  10000, "Bankrupt", "Bankrupt"]
    spun = values[random.randint(0,23)]
    goodVal = True
    if spun == "Bankrupt":
        print("You spun " + str(spun) + "!")
        goodVal = False
    else:
        print("You spun $" + str(spun) + "!")
    if goodVal:
        end = False
        while(not end):
            guess = input("Which consonant would you like to guess?: ").upper()
            if(guess not in vowels):
                end = True
            else:
                print("Sorry, that is not a consonant. Guess again.")
    count = 0
    for c in phrase:
        if c == guess:
            count +=1
    if spun == "Bankrupt":
        return [-1*winnings, guess, count]
    elif count == 0:
        return [-1*spun, guess, count]
    else:
        return [count*spun,  guess, count]


def main():
    categories = ["Before and After", "Song Lyrics", "Around the House", "Food and Drink", "Same Name"]
    PhraseBank = open("phrasebank.txt").read().splitlines()
    index = random.randint(0,99)
    phrase = PhraseBank[index]
    phraseHidden = ""
    for c in phrase:
        if c != " ":
            phraseHidden += "_ "
        else:
            phraseHidden += "  "
    winnings = 0
    print("Welcome to the Wheel of Fortune!")
    end = False
    consonantsGuessed = []
    vowelsGuessed = []
    while not end:
        print()
        print("The phrase is:")
        print(phraseHidden)
        #print(phrase)
        print("The category is: " + categories[index//20])
        print()
        print("Winnings so far: $" + str(winnings))
        print()
        print("consonants guessed: " + str(consonantsGuessed))
        print("vowels guessed: "+str(vowelsGuessed))
        move = input("Would you like to spin the wheel (type \'spin\'), \n buy a vowel for $250 (type \'vowel\'), \n or solve the puzzle (type \'solve\')?\n ").upper()
        result = [0]
        if(move == "SPIN"):
            result = spinTheWheel(phrase, winnings)
            if(result[0] != -1*winnings):
                print(str(result[1]) + " appears in the phrase " + str(result[2]) + " times.")
                print("You\'ve recieved $" + str(result[0]))
                phraseHidden = replaceLetters(phrase, phraseHidden, result[1])
                consonantsGuessed.append(result[1])
        elif(move == "VOWEL" and winnings>=250):
            print("OK! $250 will be deducted from your winnings.")
            result = buyAVowel(phrase, winnings)
            print(str(result[1]) + " appears in the phrase " + str(result[2]) + " times.")
            phraseHidden = replaceLetters(phrase, phraseHidden, result[1])
            vowelsGuessed.append(result[1])
        elif(move == "VOWEL"):
            print("Not enough money. Sorry!")
        elif(move == "SOLVE"):
            result = solveThePuzzle(phrase, winnings)
            if result[1]:
                end = True

        winnings += result[0]
    print("You ended the game with $" + winnings)


if __name__ == "__main__":
    main()
