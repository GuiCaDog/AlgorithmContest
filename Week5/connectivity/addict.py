import sys
from collections import deque

def searchAugmentingPath(s, t, resG):
        exploring = deque()
        exploring.append(s)

        pred = [0]*(2*n) 
        visited = [0]*(2*n) 

        #DFS keeping predecessors
        while visited[t] == 0 and len(exploring) != 0:
            exp = exploring.pop()
            visited[exp] = 1

            for city in resG[exp].keys():
                if visited[city] != 1 and resG[exp][city] > 0:
                    exploring.append(city)
                    pred[city] = exp
                    if city == t:
                        visited[city] = 1
                        break

        if visited[t] !=0: 
            cF = 10000
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
        
        net = [0]*(2*n)
        resi = [0]*(2*n)
        for i in range(1, 2*n):
            net[i] = {}
            resi[i] = {}
        #net
        for i in range(0, m):
            a, b = map(int, sys.stdin.readline().split())
            a2=a
            b2=b
            if a != 1 and a != n:
                a2 = a + n
                net[a][a2] = 0
                net[a2][a] = 0
                resi[a][a2] = 1
                resi[a2][a] = 1
            if b != 1 and b != n:
                b2 = b + n
                net[b][b2] = 0
                net[b2][b] = 0
                resi[b][b2] = 1
                resi[b2][b] = 1
            #a - > b
            net[a2][b] = 0 
            resi[a2][b] = 500
            #b -> a
            net[b2][a] = 0
            resi[b2][a] = 500

        #print(net)
        #print(resi)
        
        path = searchAugmentingPath(1, n, resi)
        while path != -1:
            cP = path[1]
            path = path[0]
            #if cP == 500:
            #    print(path)
            for i in range(0, len(path)-1):
                a = path[i]
                b = path[i+1]

                #flow aument a -> b
                if net[a].get(b, -1) != -1:
                    net[a][b] += cP
                    resi[b][a] = resi[b].get(a,0) + net[a][b]
                    resi[a][b] -= cP
                #flow b -> a diminish
                else:
                    net[b][a] -= cP
                    #if there is less flow b -> a
                    #a -> b you've got less capacity
                    resi[a][b] -= cP
                    #you've got more capacity b -> a now
                    resi[b][a] += cP
            path = searchAugmentingPath(1, n, resi)


        maxFlow = 0
        for b in net[1].keys():
            maxFlow += net[1][b]
        
        print("Case #{0}: {1}".format(case, maxFlow))

        if case < case_count:
            input()
