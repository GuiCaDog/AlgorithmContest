import sys


def areWeDelicious(ourMuff, mufLov, judgesLeft, jLsize, i, m):

    if jLsize == 0:
        return "yes"

    if i > m:
        return "no"
    
    #if i is liked by one of the remaining judges
    iWorth = False
    for jud in mufLov.get(i, []):
        if judgesLeft[jud] == 1:
            iWorth = True
            break

    #if -i is liked by one of the remaining judges
    iMinusWorth = False
    for jud in mufLov.get(-i, []):
        if judgesLeft[jud] == 1:
            iMinusWorth = True
            break

    if iWorth:
        ouMuAux = []
        for muf in ourMuff:
            ouMuAux.append(muf)

        juLeAux = []
        for jud in judgesLeft:
            juLeAux.append(jud)
        
        jLAuxS = jLsize
        for jud in mufLov.get(i, []):
            if juLeAux[jud] == 1:
                jLAuxS -= 1
                juLeAux[jud] = 0

        ouMuAux[i] = i

        if areWeDelicious(ouMuAux, mufLov, juLeAux, jLAuxS, i+1, m) == "yes":
            return "yes"

    if iMinusWorth:
        ouMuAux = []
        for muf in ourMuff:
            ouMuAux.append(muf)

        juLeAux = []
        for jud in judgesLeft:
            juLeAux.append(jud)
        
        jLAuxS = jLsize
        for jud in mufLov.get(-i, []):
            if juLeAux[jud] == 1:
                jLAuxS -= 1
                juLeAux[jud] = 0

        ouMuAux[i] = -i

        if areWeDelicious(ouMuAux, mufLov, juLeAux, jLAuxS, i+1, m) == "yes":
            return "yes"

    if False==iWorth and False==iMinusWorth:
        if areWeDelicious(ourMuff, mufLov, judgesLeft, jLsize, i+1, m) == "yes":
            return "yes"

    return "no"




if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        m,n = map(int, sys.stdin.readline().split()) 

        mufLov = {}
        for i in range(1, n+1):
            mufIi = [int(f) for f in sys.stdin.readline().split()]
            mufIi.pop()

            for muf in mufIi:
                mufLov[muf] = mufLov.get(muf, [])
                mufLov[muf].append(i)
        
        yesNo = areWeDelicious([0]*(m+1), mufLov, [1]*(n+1), n, 1, m)
        print("Case #{0}: {1}".format(case, yesNo))
        #print(mufLov)

        if case < case_count:
            pass#input()
