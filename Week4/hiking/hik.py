import sys
import heapq


if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n, m = map(int, sys.stdin.readline().split())
        

        parking = [0]*(n+1)
        #########################################
        for i in range(0, len(parking)):
            parking[i] = []
        for i in range(0, m):
            v,w,c = map(int, sys.stdin.readline().split())
            parking[v].append((c,w))
            parking[w].append((c,v))

        dist = [2000]*(n+1)
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
                for neigh in parking[v]:
                    w = neigh[1]
                    if dist[v] + neigh[0] < dist[w]:
                        #pqDist.remove((dist[w],w))
                        dist[w] = dist[v] + neigh[0]
                        heapq.heappush(pqDist, (dist[w], w))

        
        print("Case #{0}: {1}".format(case, dist[n]))

        if case < case_count:
            input()
