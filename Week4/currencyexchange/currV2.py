import sys
from collections import deque 
import math

if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n, m = map(int, sys.stdin.readline().split())
        

        currencies  = [0]*(n+1)
        #########################################
        for i in range(0, len(currencies)):
            currencies[i] = {}
        for i in range(0, m):
            a,b,c = sys.stdin.readline().split()
            currencies[int(a)][int(b)] = float(c)

        dist = [10000]*(n+1)
        dist[1] = 0

        phase = deque([1])
        nextPhase = {}

        pred = [0]*(n+1)
        for nPhase in range(1, n+1):
            while len(phase) != 0:
                v = phase.popleft() 
                for w in currencies[v].keys():
                    if dist[v] + math.log(currencies[v][w]) < dist[w]:
                        dist[w] = dist[v] + math.log(currencies[v][w])
                        pred[w] = v
                        nextPhase[w] = 1

            for key in nextPhase.keys():
                phase.append(key)
            nextPhase = {}
        if len(phase) != 0:
            x = "Jackpot"
        else:
            x = "impossible"
            if dist[n] < 10000:
                pre = n
                bestSequence = [n]
                while pre != 1:
                    bestSequence.append(pred[pre])
                    pre = pred[pre]

                bestExch = 1

                #looop in inverse order
                j = len(bestSequence) - 1 
                while j != 0:
                    bestExch *= currencies[bestSequence[j]][bestSequence[j-1]]
                    j-=1
                x = bestExch


        
        print("Case #{0}: {1}".format(case, x))

        if case < case_count:
            input()
