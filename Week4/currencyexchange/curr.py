import sys
import heapq
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

        pqDist = []
        for i in range(1, len(dist)):
            heapq.heappush(pqDist, (dist[i], i))
        
        pred = [0]*(n+1)
        visited = [0]*(n+1)
        while len(pqDist) != 0:
            ve = heapq.heappop(pqDist)
            v = ve[1]
            if visited[v] == 0:
                visited[v] = 1
                for w in currencies[v].keys():
                    if dist[v] + currencies[v][w] < dist[w]:
                        dist[w] = dist[v] + math.log(currencies[v][w])
                        heapq.heappush(pqDist, (dist[w], w))
                        pred[w] = v
        
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
