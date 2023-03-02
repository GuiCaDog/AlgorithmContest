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

        #initialize 4 best
        for i in range(0,10):
            pairWeights[bestPairs[i]] = 10

        entriesSum = 100
        
        i = 9
        

        while i > 0 and entriesSum != 0:
            pair = bestPairs[i]
            #not in diagonal
            if pair!=10 and pair!=8 and pair!=5 and pair!=1:
                #weight of this pair was already 10
                if pairWeights[pair] == 10:
                    #we've already put x pairs to -10, so the next has to go to 0
                    if entriesSum == 10:
                        entriesSum-=10
                        pairWeights[pair] = 0

                    #we put one that was 10 to -10, so in total -20
                    else:
                        entriesSum-= 20
                        pairWeights[pair] = -10

                #weight of this pair was 0, so we turn it to -10
                else:
                    entriesSum-=10
                    pairWeights[pair] = -10
            else:
                pairWeights[pair] = 0
                entriesSum -= 10

            i-=1


        
        #how many 10 in the diag?

        tensInDiag = 0

        if pairWeights[1] == 10:
            tensInDiag +=1
        if pairWeights[5] == 10:
            tensInDiag +=1
        if pairWeights[8] == 10:
            tensInDiag +=1
        if pairWeights[10] == 10:
            tensInDiag +=1

        i = 0 #fix matrix for those who are already in diag
        while i < 10 and tensInDiag > 0:
            pair = bestPairs[i]
            if pairWeights[pair] == -10:
                pairWeights[pair] = -5
                tensInDiag -= 1
            i+=1
        
        #who's not in diag and
        notInDiag = []
        #get pairs that are -10
        negatives = []
        #get pairs that are 10
        positives = []
        #get pairs that are 0 and not diag
        zeros = []
        i = 0
        while i < 10:
            pair = bestPairs[i]
            if pairWeights[pair] == -10:
                negatives.append(pair)
            if (pairWeights[pair] == 0 and
                    (pair==1 or pair==5 or pair==8 or pair==10)):
                notInDiag.append(pair)
            elif pairWeights[pair] == 0:
                zeros.append(pair)
            if (pairWeights[pair] == 10 and
                    (pair!=1 and pair!=5 and pair!=8 and pair!=10)):
                positives.append(pair)
            i+=1

        #print("\n", positives, notInDiag, negatives)
        #check if not in diag should be in diag
        for diagPair in notInDiag:
            #dWeight = pairWeights[diagPair]
            dCount = countPairs[diagPair]
            
            #nWeight = pairWeights[negatives[0]]
            if len(negatives) > 0:
                nCount = countPairs[negatives[0]]

            #pWeight = pairWeights[positives[-1]]
            if len(positives) > 0:
                pCount = countPairs[positives[-1]]

            if len(zeros) > 0:
                zCount = countPairs[zeros[0]]

            if (len(negatives) > 0 and len(positives) > 0 and
                10 * dCount - 10 * nCount / 2 > 10 * pCount - 10 * nCount):
                pairWeights[diagPair] = 10
                pairWeights[negatives[0]] = -5
                pairWeights[positives[-1]] = 0
                negatives = negatives[1:]
                positives = positives[:-1]

            elif len(zeros) > 0 and 10*dCount > 5*zCount:
                pairWeights[diagPair] = 10
                pairWeights[zeros[0]] = -5
                zeros = zeros[1:]

           # print(positives, negatives)
        
        notInDiag = []
        fives = []
        i = 0
        while i < 10:
            pair = bestPairs[i]
            if pairWeights[pair] == -5:
                fives.append(pair)

            if (pairWeights[pair] == 0 and
                    (pair==1 or pair==5 or pair==8 or pair==10)):
                notInDiag.append(pair)
            i+=1

        for diagPair in notInDiag:
            dCount = countPairs[diagPair]
            #nWeight = pairWeights[negatives[0]]
            if len(fives) > 0:
                fCount = countPairs[fives[-1]]

            if len(fives) > 0 and 10*dCount > 5*fCount:
                pairWeights[diagPair] = 10
                pairWeights[fives[-1]] -= 5
                fives = fives[:-1]

        fives = []
        i = 0
        while i < 10:
            pair = bestPairs[i]
            if pairWeights[pair] == -5:
                fives.append(pair)
            i+=1

        if len(fives) > 1:
            pairWeights[fives[-1]] = -10
            pairWeights[fives[0]]=0
        #now check score
        score = 0
        for i in range(1, 11):
            score += countPairs[i] * pairWeights[i]

        #print(countPairs, pairWeights)
        print("Case #{0}: {1}".format(case, score))
        print(pairWeights)



        if case < case_count:
            input()
