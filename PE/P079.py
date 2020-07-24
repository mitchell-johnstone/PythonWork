# A common security method used for online banking
# is to ask the user for three random characters
# from a passcode. For example, if the passcode
# was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.
# The text file, keylog.txt, contains fifty successful login attempts.
# Given that the three characters are always asked
# for in order, analyse the file so as to determine
# the shortest possible secret passcode of unknown length.
from decorators import *
import numpy as np
import math


def getListOfLogins():
    f = open("p079_keylog.txt")
    yield (str(n) for n in f.readlines())


def fit(numberToFit, passcode):
    tempCodes = []
    firstChar = numberToFit[0]
    for p in passcode:
        for i in range(len(p)):
            if p[i] == firstChar:
                tempcodes += p[:i] + numberToFit + p[i+1:]
                for end in fit(numberToFit[1:],p[i+1:]):
                    tempcodes += p[:i] + end
    return tempcodes


def v1():
    passcode = []
    for n in getListOfLogins():
        print(n)
        continue
        if not passcode: passcode = [n]
        else:
            tempcodes = []
            for p in passcode:
                tempcodes += fit(n,p)


@timer
def main():
    v1()


if __name__ == '__main__':
    main()
