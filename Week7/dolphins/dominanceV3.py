import sys

def argsort(seq):
    # http://stackoverflow.com/questions/3071415/efficient-method-to-calculate-the-rank-vector-of-a-list-in-python
    return sorted(range(len(seq)), reverse=True, key=seq.__getitem__)

if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n, m = map(int, sys.stdin.readline().split())
        
        actgTo1234= {"AA":1, "AC":2, "CA":2, "AT":3, "TA":3, "AG":4, "GA":4,
                     "CC":5, "CT":6, "TC":6, "CG":7, "GC":7,
                     "TT":8, "TG":9, "GT":9, "GG":10}
        
        human = []
        for i in range(0, n):
            h = sys.stdin.readline()[:-1]
            human.append(h)
            
        mice = []
        for i in range(0, m):
            mi = sys.stdin.readline()[:-1]
            mice.append(mi)
        
        countPairs = [0]*(11)
        countPairs[0] = -1

        for hu in human:
            for mi in mice:
                for i in range(0, len(hu)):
                    pair = hu[i] + "" + mi[i]
                    countPairs[actgTo1234[pair]] +=1

        bestPairs = argsort(countPairs)

        pairWeights = [0]*11
        
        
        noDiag = []
        diag = []
        #getting pairs in order of increasing number of matches 
        for i in range(0, 10):
            pair = bestPairs[i]
            if pair== 1 or pair==5 or pair==8 or pair==10:
                diag.append(pair)
            else:
                noDiag.append(pair)

        maxP = 0
        minN = 5
        mDiag = 0
        while maxP < minN:
            pCount = countPairs[noDiag[maxP]]
            nCount = countPairs[noDiag[minN]]
            dCount = 0
            if mDiag < 4:
                dCount = countPairs[diag[mDiag]]
            
            #minN is half full, but there's still another possible to be negative
            if pairWeights[noDiag[minN]] == -5 and minN - 1 > maxP:
                nCount2 = pairWeights[noDiag[minN-1]]

                #worth to add maxP
                if pCount > 2*dCount:
                    pairWeights[noDiag[maxP]] = 10
                    pairWeights[noDiag[minN]] = -10
                    pairWeights[noDiag[minN-1]] = -5
                    maxP+=1
                    minN-=1
                
                #worth to add mDiag
                else:
                    pairWeights[diag[mDiag]] = 10
                    pairWeights[noDiag[minN]] = -10
                    mDiag+=1
                    minN-=1

                
            #nCount is the last that can be negative
            elif pairWeights[noDiag[minN]] == -5:
                if pCount> 2*dCount:
                    pairWeights[noDiag[maxP]] = 5 
                    pairWeights[noDiag[minN]] = -10
                    minN-=1

                else:
                    pairWeights[diag[mDiag]] = 10 
                    pairWeights[noDiag[minN]] = -10
                    mDiag+=1
                    minN-=1
            
            #general case, weight of minN is still 0
            else:
                if pCount > 2*dCount:
                    pairWeights[noDiag[maxP]] = 10
                    pairWeights[noDiag[minN]] = -10
                    maxP+=1
                    minN-=1
                else:
                    pairWeights[diag[mDiag]] = 10
                    pairWeights[noDiag[minN]] = -5
                    mDiag+=1

        if mDiag < 4 and pairWeights[noDiag[minN]] == 0:
            nCount = countPairs[noDiag[minN]]
            dCount = countPairs[diag[mDiag]]
            if dCount*10 > nCount*5:
                pairWeights[diag[mDiag]] = 10
                pairWeights[noDiag[minN]] = -5
                mDiag += 1
        if mDiag < 4 and pairWeights[noDiag[minN]] == -5:
            nCount = countPairs[noDiag[minN]]
            dCount = countPairs[diag[mDiag]]
            if dCount*10 > nCount*5:
                pairWeights[diag[mDiag]] = 10
                pairWeights[noDiag[minN]] = -10



        #now check score
        score = 0
        for i in range(1, 11):
            score += countPairs[i] * pairWeights[i]

        print("Case #{0}: {1}".format(case, score))
        
        print(countPairs, pairWeights)

        if case < case_count:
            input()
