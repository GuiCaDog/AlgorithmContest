import sys
import re

if __name__ == '__main__':

    s = re.compile(r"[a-z]+")
    d = re.compile(r"[0-9]+")


    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):

        line = input()

        #Getting the numbers and the operations
        opsIter = list(s.finditer(line))
        nmbrsIter = list(d.finditer(line))

        #Starting the calculation
        result = int(nmbrsIter[0].group())
        i = 1

        #Mapping string to operation
        while i < len(nmbrsIter):

            if opsIter[i-1].group() == "plus":
                result += int(nmbrsIter[i].group())

            if opsIter[i-1].group() == "minus":
                result -= int(nmbrsIter[i].group())

            if opsIter[i-1].group() == "times":
                result *= int(nmbrsIter[i].group())

            if opsIter[i-1].group() == "tothepowerof":
                result = pow(result, int(nmbrsIter[i].group()))
            i+=1




        print("Case #{0}: {1}".format(case, result))
