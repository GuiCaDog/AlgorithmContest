import sys
from collections import deque

def searchAugmentingPath(s, t, resG):
        exploring = deque()
        exploring.append(s)


        pred = [-1]*(len(resG)) 
        visited = [-1]*(len(resG)) 

        #DFS keeping predecessors
        while visited[t] == -1 and len(exploring) != 0:
            exp = exploring.pop()
            visited[exp] = 1
            for food in resG[exp].keys():
                if visited[food] != 1 and resG[exp][food] > 0:
                    exploring.append(food)
                    pred[food] = exp
                    if food == t:
                        visited[food] = 1
                        break


        if visited[t] !=-1: 
            pre = t
            path = deque([t])
            while pre != s:
                #w = resG[pred[pre]][pre]
                #if w < cF:
                #    cF = w
                path.appendleft(pred[pre])
                pre = pred[pre]
            return [path, 1]
        else:
            return -1


if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n, m, b= map(int, sys.stdin.readline().split())
        
        net = [0]*(m+b+2)
        resi = [0]*(m+b+2)
        for i in range(0, len(net)):
            net[i] = {}
            resi[i] = {}
        for i in range(1, m+1):
            net[0][i]=0
            resi[0][i]=1
        #net
        for i in range(0, n):
            d, l = map(int, sys.stdin.readline().split())
            #a - > b
            l = l + m
            net[d][l] = 0 
            net[l][m+b+1]=0
            resi[d][l] = 1
            resi[l][m+b+1]=1
        

        #print(net, resi)
        path = searchAugmentingPath(0, m+b+1, resi)
        while path != -1:
            cP = path[1]
            path = path[0]
            for i in range(0, len(path)-1):
                u = path[i]
                v = path[i+1]

                #flow aument u -> v
                if net[u].get(v, -1) != -1:
                    net[u][v] += cP
                    resi[v][u] = net[u][v]
                    resi[u][v] -= cP
                #flow v -> u diminish
                else:
                    net[v][u] -= cP
                    #if there is less flow b -> a
                    #a -> b you've got less capacity
                    resi[u][v] -= cP
                    #you've got more capacity b -> a now
                    resi[v][u] += cP
            path = searchAugmentingPath(0, m+b+1, resi)


        maxFlow = 0
        for v in net[0].keys():
            maxFlow += net[0][v]
        if maxFlow == 0:
            maxFlow = "impossible"
        
        print("Case #{0}: {1}".format(case, maxFlow))
        if case < case_count:
            input()
