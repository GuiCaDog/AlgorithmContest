import sys

def getStories(seq, chaptsPut, i, charChapt, chapPred, n, nChapts): 

    if i > nChapts:
        return 1
    
    nValidStories = 0
    #next possible chapters
    pred = seq[i-1]
    predChar = pred // 100
    for j in range(1, n+1):
        #no same character
        if j != predChar:
            #we check that there are chapters of this character left to put
            if chaptsPut[j] + 1 <= charChapt[j]:
                nextChapt =j*100 + chaptsPut[j] + 1
                #now nextChapt has to satisfy its dependencies
                for dep in chapPred.get(nextChapt, []):
                    c = dep[0]
                    p = dep[1]
                    #if chapter c,p d is already in the sequence
                    #chaptsPut[c] has to be greater or equal than p
                    if chaptsPut[c] < p:
                        #there's a chapter that has to go before 
                        #nextChapt, but we haven't put it already
                        #so nextChapt can't continue the sequence
                        break
                else: #all dependencies of nextChapt are satisfied
                    sAux = []
                    for chap in seq:
                        sAux.append(chap)

                    cPutAux = []
                    for chapt in chaptsPut:
                        cPutAux.append(chapt)

                    cPutAux[j] += 1
                    sAux[i] = nextChapt
                    nValidStories += getStories(sAux, cPutAux, i+1, charChapt, chapPred, n, nChapts)
    return nValidStories


if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n,m = map(int, sys.stdin.readline().split()) 
        charChapts = [0]*(n+1)
        nChapts = 0
        for i in range(1, n+1):
            charChapts[i] = int(input())
            nChapts += charChapts[i]
        
        chapPred = {}

        for i in range(0, m):
            c, p, d, q = map(int, sys.stdin.readline().split())
            suc = d*100 + q
            pred = (c,p)
            chapPred[suc] = chapPred.get(suc, [])
            chapPred[suc].append(pred)

        k = getStories([0]*(nChapts+1),[0]*(n+1), 1, charChapts, chapPred, n, nChapts) 
        print("Case #{0}: {1}".format(case, k))

        if case < case_count:
            input()
