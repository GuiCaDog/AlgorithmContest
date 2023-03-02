import sys
import heapq


if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n, m, k = map(int, sys.stdin.readline().split())
        

        city = [0]*(n+1)
        #########################################
        for i in range(0, len(city)):
            city[i] = {}

        leasPath = sys.stdin.readline().split()
        leasPath = [int(j) for j in leasPath]

        for i in range(0, m):
            a,b,c = map(int, sys.stdin.readline().split())
            if city[a].get(b, -1) == -1:
                city[a][b] = []
                city[b][a] = []
            city[a][b].append(c)
            city[b][a].append(c)

        cMinPath = 0
        leaEdges = [0]*(len(leasPath)-1)
        for i in range(0, len(leasPath) - 1):
            v = leasPath[i]
            w = leasPath[i+1]
            f = lambda i: city[v][w][i]
            leaEdges[i] = min(range(len(city[v][w])), key = f) 
            cMinPath += city[v][w][leaEdges[i]]
        
        x = "no"

        for i in range(0, len(leasPath) - 1):
            aIg = leasPath[i]
            bIg = leasPath[i+1]
            cIg = leaEdges[i]
            realCost = city[aIg][bIg][cIg]
            city[aIg][bIg][cIg] = 20000

            dist = [20000000000]*(n+1)
            dist[1] = 0
            pqDist = []
            for i in range(1, len(dist)):
                heapq.heappush(pqDist, (dist[i], i))
            
            visited = [0]*(n+1)
            while len(pqDist) != 0:
                ve = heapq.heappop(pqDist)
                v = ve[1]
                if visited[v] == 0:
                    visited[v] = 1
                    for w in city[v]:
                        c = min(city[v][w])
                        if dist[v] + c < dist[w]:
                            dist[w] = dist[v] + c
                            heapq.heappush(pqDist, (dist[w], w))

            if dist[n] == cMinPath:
                x = "yes"
                break

            city[aIg][bIg][cIg] = realCost
        
        print("Case #{0}: {1}".format(case, x))

        if case < case_count:
            input()
