import sys

def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)


if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n, m = map(int, sys.stdin.readline().split())
        
        facilitiesCost = [-1] + [int(l) for l in sys.stdin.readline().split()]
        facilitiesPref = [-1]*(n+1)
        customersPref = [-1]*(m+1)
        customersPrefIndex = [-1]*(m+1)

        actives = [-1] + [0]*(n)
        facilitiesServing = [-1]*(n+1)

        for c in range(1, m+1):
            customersPref[c] = []
            customersPrefIndex[c] = []
        for i in range(1, n+1):
            facilitiesPref[i] = [int(c) for c in sys.stdin.readline().split()]
            facilitiesServing[i] = {}
        
        #creating customers preferences
        for c in range(1, m+1):
            for f in range(1, n+1):
                customersPref[c].append(facilitiesPref[f][c-1])

        for c in range(1, m+1):
            customersPrefIndex[c] = argsort(customersPref[c])
            for f in range(0, n):
                customersPrefIndex[c][f] += 1
        
        #initial state
        for c in range(1, m+1):
            actives[customersPrefIndex[c][0]] = 1
            facilitiesServing[customersPrefIndex[c][0]][c] = 1
        
        bestR = -2
        while bestR != -1:
            #step: looking for the "best" facility removal
            bestR = -1
            bestRImprov = 0
            activatedInBest = []
            bestMovements = {}
            for f in range(1, n+1):
                if actives[f] == 1:
                    fCost = facilitiesCost[f]
    
                    #where is cheapest to move the customers?
                    movingSum = 0
                    activatedFacilities = []
                    movements = {} 
                    tempActives = []
                    for a in actives:
                        tempActives.append(a)
    
                    for c in facilitiesServing[f].keys():
                        
    
                        cheapestCostForC = 100000000000
                        cheapestMove = -1
                        
                        #where is cheapest to move this consumer?
                        for i in range(0, n):
                            nextFacility = customersPrefIndex[c][i]
                            if nextFacility == f:
                                pass
                            else:
                                costForC = 0
                                if tempActives[nextFacility] == 0:
                                    costForC = facilitiesCost[nextFacility] + facilitiesPref[nextFacility][c-1]- facilitiesPref[f][c-1]
                                    if costForC < cheapestCostForC:
                                        cheapestCostForC = costForC
                                        cheapestMove = nextFacility
                                else:
                                    costForC = facilitiesPref[nextFacility][c-1] - facilitiesPref[f][c-1]
                                    if costForC < cheapestCostForC:
                                        cheapestCostForC = costForC    
                                        cheapestMove = nextFacility
                                    break
                            
                        if tempActives[cheapestMove] == 0:
                            tempActives[cheapestMove] = 1
                            activatedFacilities.append(cheapestMove)
                        movements[c]=cheapestMove
                        movingSum += cheapestCostForC
                    #print(f, fCost, movingSum)
                    if fCost - movingSum > bestRImprov:
                        bestRImprov = fCost - movingSum
                        bestR = f
                        activatedInBest = []
                        for a in activatedFacilities:
                            activatedInBest.append(a)
    
                        bestMovements = {} 
                        for m in movements.keys():
                            bestMovements[m] = movements[m]
    
            #step: update improve
            if bestR != -1:
                for a in activatedInBest:
                    actives[a] = 1 

                actives[bestR] = 0
            
                for c in bestMovements.keys():
                    facilitiesServing[bestR].pop(c, None)
                    facilitiesServing[bestMovements[c]][c] = 1
    
        totalCost = 0
        for f in range(1, n+1):
            if actives[f] == 1:
                totalCost += facilitiesCost[f]
            for c in facilitiesServing[f].keys():
                totalCost += facilitiesPref[f][c-1]

        print("Case #{0}: {1}".format(case, totalCost))
        
        #print(actives)
        for i in range(1, n+1):
            res = "" + str(i)+ " "
            for c in facilitiesServing[i].keys():
                res+= str(c) + " "
            res = res[:-1]
            if actives[i] == 1:
                print(res)
        #for i in range(1, m+1):
        #    print(customersPref[i])
        #for i in range(1, m+1):
        #    print(customersPrefIndex[i])

        #print(bestR, bestRImprov, activatedInBest, bestMovements)
        if case < case_count:
            input()
