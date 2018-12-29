import random

def solveThePuzzle(solution, balance):
    print()
def buyAVowel(solution, balance):
    print()
def spinTheWheel(solution, balance):
    print()
def main():
  print("Welcome to the Wheel of Fortune!")
  PhraseBank = open("phrasebank.txt").read().splitlines()
  index = random.randint(1,101);
  phrase = PhraseBank[index]
  print(phrase)

if __name__ == "__main__":
  main()
