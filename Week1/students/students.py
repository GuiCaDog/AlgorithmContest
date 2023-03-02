import sys
import re


if __name__ == '__main__':

    tinTen = re.compile(r"entin|enten")
    ent = re.compile(r"ent")

    print("Case #{0}: {1}".format("1", ""))

    sys.stdin.readline()
    nLines = int(sys.stdin.readline())

    for nLine in range(1, nLines + 1):
        line = input()

        #Changing entin and enten first
        newLine = ""
        newLineC = 0
        
        for match in tinTen.finditer(line):
            newLine += (line[newLineC:match.start()] + "ierende")
            newLineC = match.start() + 5

        newLine += line[newLineC:]

        #Now we change ent
        outLine = ""
        outLineC = 0
        for match in ent.finditer(newLine):
            outLine += (newLine[outLineC:match.start()] + "ierender")
            outLineC = match.start() + 3

        outLine += newLine[outLineC:]
            

        print(outLine)
