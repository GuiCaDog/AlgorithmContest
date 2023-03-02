import sys
def argsort(seq):
    # http://stackoverflow.com/questions/3071415/efficient-method-to-calculate-the-rank-vector-of-a-list-in-python
    return sorted(range(len(seq)), key=seq.__getitem__, reverse=True)

def minCoins(amount, coinTypes, amountsSolved):
    if amountsSolved.get(amount,None) is not None:
        return sum(amountsSolved[amount]), amountsSolved[amount]
    else:
        minAmount = -1
        minC= None
        iMin = -1
        for i in range(len(coinTypes)-1):
            c = coinTypes[i]
            if amount-c >=0:
                amountAux, aSAux = minCoins(amount-c, coinTypes, amountsSolved)
                if amountAux < minAmount or minAmount == -1:
                    minAmount = amountAux
                    minC = aSAux
                    iMin = i

        if minAmount == -1:
            res = [0]*(len(coinTypes)-1)
            res.append(amount)
            return amount, res 
        else:

            amountsSolved[amount] = [0]*len(coinTypes)
            for i in range(len(minC)):
                amountsSolved[amount][i] = minC[i]

            amountsSolved[amount][iMin] += 1
            return sum(amountsSolved[amount]), amountsSolved[amount]



if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n, a = map(int, sys.stdin.readline().split())
        
        counts = {}
        coins = [int(i) for i in sys.stdin.readline().split()]
        sortedIndex = argsort(coins)
        coins.sort(reverse=True)
        for i in range(len(coins)):
            c = coins[i]
            counts[c] = [0]*n
            counts[c][i] += 1
        
        counts[0] = [0]*n
        p, b = minCoins(a, coins, counts)
        sol = ""
        res = [0]*n
        for i in range(n):
            res[i] = b[sortedIndex[i]]

        for c in res:
            sol+= str(c)
            sol+=" "

        sol = sol[:-1]
        print("Case #{0}: {1}".format(case, sol))
        #print(coins, counts)
        #print(p, b)

        if case < case_count:
            input()
