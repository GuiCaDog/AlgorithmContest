import sys
def argsort(seq):
    # http://stackoverflow.com/questions/3071415/efficient-method-to-calculate-the-rank-vector-of-a-list-in-python
    return sorted(range(len(seq)), key=seq.__getitem__)

if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n, a = map(int, sys.stdin.readline().split())
        
        preds = [0]*(a+1) 
        counts = [0]*n
        countTotal = [1000000]*(a+1)
        coins = [int(i) for i in sys.stdin.readline().split()]
        #for i in range(a+1):
        #    countsHash[i] = [0]*n
        
        countTotal[0] = 0
        sortedCoinIndex = argsort(coins)
        for i in range(1, a+1):
            bestCoin = 0
            for j in sortedCoinIndex: 
            #for j in range(len(coins)):
                c = coins[j]
                sub = i-c
                if sub >= 0:
                    if countTotal[sub] + 1 < countTotal[i]:
                        countTotal[i] = countTotal[sub] + 1
                        bestCoin = j
                else:
                    break
            preds[i] = [bestCoin, i - coins[bestCoin]]
        
        i = a
        while i > 0:
            counts[preds[i][0]]+=1
            i = preds[i][1]
            #aux = []
            #for c in countsHash[i-coins[bestCoin]]:
            #    aux.append(c)

            #aux[bestCoin]+=1
            #countsHash[i] = aux 
                        

        sol = ""

        for c in counts:
            sol+= str(c)
            sol+=" "

        sol = sol[:-1]

        print("Case #{0}: {1}".format(case, sol))
        #print(countTotal[a])

        if case < case_count:
            input()
