# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:
#
# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
#
# If two players have the same ranked hands then the rank made up of the highest value wins;
# for example, a pair of eights beats a pair of fives (see example 1 below).
# But if two ranks tie, for example, both players have a pair of queens,
# then highest cards in each hand are compared (see example 4 below);
# if the highest cards tie then the next highest cards are compared, and so on.
#
# Consider the following five hands dealt to two players:
#
# Hand	 	Player 1	 	Player 2	 	Winner
# 1	 	5H 5C 6S 7S KD
# Pair of Fives
#  	2C 3S 8S 8D TD
# Pair of Eights
#  	Player 2
# 2	 	5D 8C 9S JS AC
# Highest card Ace
#  	2C 5C 7D 8S QH
# Highest card Queen
#  	Player 1
# 3	 	2D 9C AS AH AC
# Three Aces
#  	3D 6D 7D TD QD
# Flush with Diamonds
#  	Player 2
# 4	 	4D 6S 9H QH QC
# Pair of Queens
# Highest card Nine
#  	3D 6D 7H QD QS
# Pair of Queens
# Highest card Seven
#  	Player 1
# 5	 	2H 2D 4C 4D 4S
# Full House
# With Three Fours
#  	3C 3D 3S 9S 9D
# Full House
# with Three Threes
#  	Player 1
# The file, poker.txt, contains one-thousand random hands
# dealt to two players. Each line of the file contains ten cards (separated by a single space):
# the first five are Player 1's cards and the last five are Player 2's cards.
# You can assume that all hands are valid (no invalid characters or repeated cards),
# each player's hand is in no specific order, and in each hand there is a clear winner.
#
# How many hands does Player 1 win?
#
#-----------------------------------------------MY CODE-----------------------------------------------
#
#checks if there is any staights in the hand
#return highest card, if a straight is present
def checkStraight(hand):
    lastVal = getValueOfCard(hand[0])-1
    for card in hand:
        currentVal = getValueOfCard(card)
        if(not lastVal + 1 == currentVal):
            return 0
        lastVal = currentVal
    return getValueOfCard(hand[4])

#checks if there is a flush in the hands
#returns highest point, if flush is presenty
def checkFlush(hand):
    suit = (hand[0])[1]
    for card in hand:
        if(not suit == card[1]):
            return 0
    return getValueOfCard(hand[4])


#checks if there are 3 of the same kind in hand
#return val of the 3 of a kind if there is on
def ThreeOfAKind(hand):
    for i in range(3):
        card1 = getValueOfCard(hand[i])
        card2 = getValueOfCard(hand[i+1])
        card3 = getValueOfCard(hand[i+2])
        if(card1 == card2 and card1 == card3):
            return card2
    return 0

#checks if there are 4 of the same kind in hand
#return val of the 4 of a kind if there is on
def FourOfAKind(hand):
    for i in range(2):
        card1 = getValueOfCard(hand[i])
        card2 = getValueOfCard(hand[i+1])
        card3 = getValueOfCard(hand[i+2])
        card4 = getValueOfCard(hand[i+3])
        if(card1 == card2 and card1 == card3 and card1 == card4):
            return card2
    return 0

#finds the highest pair there is
def pair(hand):
    if(numOfPairs(hand) == 0):
        return 0

    card1 = 0
    for i in range(4,-1,-1):
        tmpCount = 0
        for j in range(4,-1,-1):
            card1 = getValueOfCard(hand[i])
            card2 = getValueOfCard(hand[j])
            if(card1 == card2):
                tmpCount += 1
        if(tmpCount == 2):
            return card1
    return 0

#finds how many pairs (and only pairs) there are
def numOfPairs(hand):
    count = 0
    for i in range(5):
        tmpCount = 0
        for j in range(5):
            card1 = getValueOfCard(hand[i])
            card2 = getValueOfCard(hand[j])
            # print(card1," : ", card2)
            if(card1 == card2):
                tmpCount += 1
        if(tmpCount == 2):
            count+=1
        # print()

    return count//2

#check if the hand is a full house
#return val based on the three of a kind
def checkFullHouse(hand):
    if(ThreeOfAKind(hand) != 0 and numOfPairs == 1):
        return ThreeOfAKind(hand)
    return 0

#returns the point value of an inputed card
def getValueOfCard(card):
    val = 0
    if(card[0] == "A"):
        val = 14
    elif(card[0] == "K"):
        val = 13
    elif(card[0] == "Q"):
        val = 12
    elif(card[0] == "J"):
        val = 11
    elif(card[0] == "T"):
        val = 10
    else:
        val = int(card[0])
    return val

#sorts the list in order of point value
def sortCards(hand):
    for i in range(len(hand)-1):
        for j in range(len(hand)-i-1):
            card = hand[j]
            val1 = getValueOfCard(card)
            card = hand[j+1]
            val2 = getValueOfCard(card)
            if(val1>val2):
                hand[j+1] = hand[j]
                hand[j] = card
    return hand

#will return 1 if first hand has higher card
#will return 0 if 2nd hand is higher
#will return 0 if same hand
#we only care if the first player wins.
def compareHands(hand1, hand2):
    straightVal1 = checkStraight(hand1)
    straightVal2 = checkStraight(hand2)

    flushVal1 = checkFlush(hand1)
    flushVal2 = checkFlush(hand2)

    # Royal Flush:
    rf1 = 0
    rf2 = 0
    if(straightVal1 == 14 and flushVal1 == 14):
        rf1 = 14
    if(straightVal2 == 14 and flushVal2 == 14):
        rf2 = 14
    if(rf1>rf2):
        return 1
    if(rf2>rf1):
        return 0

    # Straight Flush:
    sf1 = 0
    sf2 = 0
    if(straightVal1 != 0 and flushVal1 != 0):
        sf1 = straightVal1
    if(straightVal2 != 0 and flushVal2 != 0):
        sf2 = straightVal1
    if(sf1 > sf2):
        return 1
    if(sf2 > sf1):
        return 0

    # Four of a Kind:
    val1 = FourOfAKind(hand1)
    val2 = FourOfAKind(hand2)
    if(val1 > val2):
        return 1
    if(val2 > val1):
        return 0

    # Full House:
    val1 = checkFullHouse(hand1)
    val2 = checkFullHouse(hand2)
    if(val1 > val2):
        return 1
    if(val2 > val1):
        return 0

    # Flush:
    if(flushVal1 > flushVal2):
        return 1
    if(flushVal2 > flushVal1):
        return 0

    # Straight:
    if(straightVal1 > straightVal2):
        return 1
    if(straightVal2 > straightVal1):
        return 0

    # Three of a Kind:
    threeVal1 = ThreeOfAKind(hand1)
    threeVal2 = ThreeOfAKind(hand2)
    if(threeVal1 > threeVal2):
        return 1
    if(threeVal2 > threeVal1):
        return 0

    # Two Pairs:
    np1 = numOfPairs(hand1)
    np2 = numOfPairs(hand2)
    if(np1>np2):
        return 1
    if(np2>np1):
        return 0

    # One Pair:
    p1 = pair(hand1)
    p2 = pair(hand2)
    if(p1 > p2):
        return 1
    if(p2 > p1):
        return 0

    # High Card:
    for i in range(4,-1,-1):
        card1 = getValueOfCard(hand1[i])
        card2 = getValueOfCard(hand2[i])
        if(card1 > card2):
            return 1
        if(card2 > card1):
            return 0

    return 0

def main():
    Player1Wins = 0
    # print(pair(["3S","3S","5S","AS","AS"]))
    f = open("C:\\Programming\\Work\\Python\\PE\\P054_poker.txt", "r")
    # f = ["5H 5C 6S 7S KD 2C 3S 8S 8D TD","5D 8C 9S JS AC 2C 5C 7D 8S QH","2D 9C AS AH AC 3D 6D 7D TD QD","4D 6S 9H QH QC 3D 6D 7H QD QS","2H 2D 4C 4D 4S 3C 3D 3S 9S 9D"]
    for hands in f:
        cards = hands.split();
        hand1 = sortCards(cards[:5])
        hand2 = sortCards(cards[5:])
        Player1Wins+=compareHands(hand1,hand2)
    print(Player1Wins)
    return

if __name__ == '__main__':
    main()
