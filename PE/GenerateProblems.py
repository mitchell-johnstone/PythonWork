from requests import get
from os import listdir
from os.path import isfile, join

# n is the problem number to get info on
# return the content of the problem, unfiltered except for isolating the actual
# problem
def getUnfilteredProblemInfo(n):
    URL = "https://projecteuler.net/problem="
    url = URL + str(n)
    r = get(url)
    content = str(r.content)
    start = content.find("<div class=\"problem_content\" role=\"problem\">")
    start += len("<div class=\"problem_content\"role=\"problem\">") + 1
    end = content.find("<div id=\"footer\"")
    return content[start:end]

# get the content from the unfiltered problem info method, then filter out the
# tags and newlines, and split up into lines with #'s in front for comment
def getProblemInfo(n):
    content = getUnfilteredProblemInfo(n)
    text = content.split("\\n")
    newText = []
    for line in text:
        inTag = False
        backslash = False
        newLine = "# "
        for char in line:
            if char == '<': inTag = True
            elif char == '>': inTag = False
            elif backslash: backslash = False
            elif char == "\\": backslash = True
            elif not inTag:
                newLine += char
        if newLine!="# ":
            while len(newLine) > 100:
                i = newLine.find(" ",45)
                newText += [newLine[:i]]
                newLine = "# " + newLine[i+1:]
            newText += [newLine]
    return newText

def createTemplate():
    return ["from decorators import *",
            "import numpy as np",
            "import math",
            "",
            "",
            "def v1():",
            "    print()",
            "",
            "",
            "@timer",
            "def main():",
            "    v1()",
            "",
            "",
            "if __name__ == '__main__':",
            "    main()"
           ]


#writes everything to a file
def writeProblemToFile(n):
    text = getProblemInfo(n) + createTemplate()
    f=open("P"+("0"*(3-len(str(n)))) + str(n) + ".py","w+")
    for line in text:
        f.write(line + "\n")
    f.close()


# gets all the files in the directory
def getFilesInDirectory():
    return [f for f in listdir("C:\\Programming\\Work\\Python\\PE") if
                 isfile(join("C:\\Programming\\Work\\Python\\PE", f))]


def checkUpTo(n):
    problems = [1] + [0] * n
    for f in getFilesInDirectory():
        try:
            problems[int(f[1:4])] = 1
        except: continue
    return problems


def main():
    upTo = int(input("What problem to update to?  "))
    problems = checkUpTo(upTo)
    for i in range(1,upTo+1):
        if not problems[i]:
            writeProblemToFile(i)
    print("All caught up!")



if __name__ == "__main__":
    main()
