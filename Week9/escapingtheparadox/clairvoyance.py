import sys
import time
import heapq

if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n, m, g = map(int, sys.stdin.readline().split())
        #print(n) 

        temple = [0]*(n+1)
        #########################################
        for i in range(0, len(temple)):
           temple[i] = {}

        relics = sys.stdin.readline().split()
        relics = [0] + [int(j) for j in relics]
        
        for i in range(0, m):
            a,b,c = map(int, sys.stdin.readline().split())
            #print(a, n)
            if temple[a].get(b, -1) == -1:
                temple[a][b] = c 
                temple[b][a] = c 
            else:
                if temple[a][b] > c:
                    temple[a][b] = c 
                    temple[b][a] = c 
        
        if g == 0 or g == n:
            res = "impossible"
        else:
            t0 = time.time()

            
            #=========================DIJSTRA===============================# 

            dist = [20000000000]*(n+1)
            dist[g] = 0
            pqDist = []
            for i in range(1, len(dist)):
                heapq.heappush(pqDist, (dist[i], i))

            visited = [0]*(n+1)
            while len(pqDist) != 0:
                ve = heapq.heappop(pqDist)
                v = ve[1]
                if visited[v] == 0:
                    visited[v] = 1
                    for w in temple[v].keys():
                        c = temple[v][w]
                        if dist[v] + c < dist[w]:
                            dist[w] = dist[v] + c
                            heapq.heappush(pqDist, (dist[w], w))

            t1 = time.time() 
            res = -3

            #====================Initial Table===============================# 
            dynTable = [0]*dist[0]
            dynTable[0] = [-1]*(n+1)
            dynTable[0][g] = -2
            dynTable[0][n] = relics[n]

            for i in range(1, len(dynTable)):
                dynTable[i] = [-1]*(n+1)
                dynTable[i][g] = -2

            for i in range(1, len(dist)):
                for j in range(dist[i], len(dynTable)):
                    dynTable[dist[i]][i] = -2
                
            ##print(g, dynTable[0])



            #toExpand = [(0,g)]

            #visited = [-1] * (n+1)
            #
            #timeIn0 = len(dynTable)-1 
            #while len(toExpand) > 0: 
            #    toExpandAfter=[]

            #    for gr in toExpand:
            #        arrT = gr[0]
            #        grave = gr[1]
            #        visited[grave]=arrT
            #        for ady in temple[grave].keys():
            #            arrToAdy = arrT+temple[grave][ady]
            #            if ady == 0:
            #                if timeIn0 > arrToAdy:
            #                    timeIn0 = arrToAdy 
            #            if arrToAdy <= timeIn0:
            #                for i in range(arrToAdy, len(dynTable)):
            #                    dynTable[i][ady] = -2

            #                if visited[ady] > arrToAdy or visited[ady] == -1:
            #                    toExpandAfter.append((arrToAdy, ady))
            #    
            #    
            #    toExpand = toExpandAfter

            #    #dynTable = dynTable[:(timeIn0+1)]
            
            t2 = time.time()
            #====================Dynamic solving===============================# 
            #filling the table
            for t in range(len(dynTable)):
                for g in range(n+1):
                    if dynTable[t][g] == -1:
                        #check predecessors
                        bestPred = -1
                        for pred in temple[g].keys():
                            if pred > g:
                                distance = temple[g][pred]
                                tInPred = t-distance
                                if tInPred >= 0:
                                    relicsInPred = dynTable[tInPred][pred]
                                    if relicsInPred >= 0:
                                        if relicsInPred + relics[g] > bestPred:
                                            bestPred = relicsInPred + relics[g] 
                        dynTable[t][g] = bestPred

                        if g == 0 and bestPred >= 0 and bestPred > res:
                            res = bestPred
            t3 = time.time()
            
            if res == -3:
                res = "impossible"
        
        print("Case #{0}: {1}".format(case, res))
        #print(t1-t0, t2-t1, t3-t2)

        if case < case_count:
            input()
