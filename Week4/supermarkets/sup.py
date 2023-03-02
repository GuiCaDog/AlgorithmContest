import sys
import heapq


if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n, m, s, a, b = map(int, sys.stdin.readline().split())
        

        roads  = [0]*(n+1)
        shops = {}
        #########################################
        for i in range(1, n+1):
            roads[i] = {}
        for i in range(0, m):
            x,y,z = map(int, sys.stdin.readline().split())
            #we only care about the best road between 2 cities
            if x != y:
                if roads[x].get(y, -1) == -1:
                    roads[x][y] = z
                    roads[y][x] = z
                elif roads[x][y] > z:
                    roads[x][y] = z
                    roads[y][x] = z

        

        for i in range(0, s):
            c,w = map(int, sys.stdin.readline().split())
            if shops.get(c, -1) == -1:
                shops[c] = w
            #for each city, we only care about its better shop
            elif shops[c] > w:
                shops[c] = w


        dist = [1000000000]*(n+1)
        dist[a] = 0
        pqDist = []
        for i in range(1, len(dist)):
            heapq.heappush(pqDist, (dist[i], i))
        
        visited = [0]*(n+1)
        while len(pqDist) != 0:
            ve = heapq.heappop(pqDist)
            v = ve[1]
            if visited[v] == 0:
                visited[v] = 1
                for w in roads[v].keys():
                    if dist[v] + roads[v][w] < dist[w]:
                        #pqDist.remove((dist[w],w))
                        dist[w] = dist[v] + roads[v][w]
                        heapq.heappush(pqDist, (dist[w], w))

        distTom = [1000000000]*(n+1)
        distTom[b] = 0
        pqDist = []
        for i in range(1, len(distTom)):
            heapq.heappush(pqDist, (distTom[i], i))
        
        visited = [0]*(n+1)
        while len(pqDist) != 0:
            ve = heapq.heappop(pqDist)
            v = ve[1]
            if visited[v] == 0:
                visited[v] = 1
                for w in roads[v].keys():
                    if distTom[v] + roads[v][w] < distTom[w]:
                        distTom[w] = distTom[v] + roads[v][w]
                        heapq.heappush(pqDist, (distTom[w], w))
        
        bestRoute = 1000000000
        for city,shopTime in shops.items():
            route = dist[city] + shopTime + distTom[city]
            if route < bestRoute:
                bestRoute = route
        if bestRoute == 1000000000:
            bestRoute = "impossible"
        else:
            h = bestRoute // 60
            m = bestRoute % 60
            h = str(h)
            m = str(m)
            if len(m) == 1:
                m = "0"+m
            bestRoute = h+":"+m
        
        print("Case #{0}: {1}".format(case, bestRoute))

        if case < case_count:
            input()
