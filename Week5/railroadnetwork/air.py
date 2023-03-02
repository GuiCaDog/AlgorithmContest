import sys
from collections import deque

def searchAugmentingPath(s, t, resG):
        exploring = deque()
        exploring.append(s)

        pred = {}
        visited = {}

        pathFlow = 0
        for key in resG.keys():
            visited[key] = 0
        
        #DFS keeping predecessors
        while visited[t] == 0 and len(exploring) != 0:
            exp = exploring.pop()
            visited[exp] = 1

            for city in resG.get(exp,[]):
                if visited[city] != 1 and resG[exp][city] > 0:
                    exploring.append(city)
                    pred[city] = exp
                    if city == t:
                        visited[city] = 1
                        break

        if visited[t] !=0: 
            cF = 1000
            pre = n
            path = deque([t])
            while pre != s:
                w = resG[pred[pre]][pre]
                if w < cF:
                    cF = w
                path.appendleft(pred[pre])
                pre = pred[pre]
            return [path, cF]
        else:
            return -1


if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n, m = map(int, sys.stdin.readline().split())
        
        trains = {} #[0]*(n+1)
        resTrains = {} #[0]*(n+1)
        for i in range(1, n+1):
            trains[i] = {}
            resTrains[i] = {}
        for i in range(0, m):
            a, b, w = map(int, sys.stdin.readline().split())
            if a != b:
                #a - > b
                capFlow = trains[a].get(b, [0, 0])
                capFlow[0] += w
                trains[a][b] = capFlow 
                #b -> a
                capFlow = trains[b].get(a, [0, 0])
                capFlow[0] += w
                trains[b][a] = capFlow 

        net = {} #[0]*(n+1)
        resi = {} #[0]*(n+1)
        for i in range(1, n+1):
            net[i] = {}
            resi[i] = {}
        for a in list(trains.keys()):
            for b in list(trains[a].keys()):
                w = trains[a][b][0]
                m = str(a)+"."+str(b)
                net[a][m] = [w, 0]
                net[m] = {}
                net[m][b] = [w, 0]
                resi[a][m] = w
                resi[m] = {}
                resi[m][b] = w

        path = searchAugmentingPath(1, n, resi)
        while path != -1:
            cP = path[1]
            path = path[0]
            for i in range(0, len(path)-1):
                a = path[i]
                b = path[i+1]

                #flow aument a -> b
                if net[a].get(b, -1) != -1:
                    net[a][b][1] += cP
                    resi[b][a] = net[a][b][1]
                    resi[a][b] -= cP
                #flow b -> a diminish
                else:
                    net[b][a][1] -= cP
                    #if there is less flow b -> a
                    #a -> b you've got less capacity
                    resi[a][b] -= cP
                    #you've got more capacity b -> a now
                    resi[b][a] += cP
            path = searchAugmentingPath(1, n, resi)


        maxFlow = 0
        for b in net[1].keys():
            maxFlow += net[1][b][1]
        if maxFlow == 0:
            maxFlow = "impossible"
        
        print("Case #{0}: {1}".format(case, maxFlow))

        if case < case_count:
            input()
