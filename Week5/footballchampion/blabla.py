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
        n, numM = map(int, sys.stdin.readline().split())
        wins = [0] + [int(i) for i in sys.stdin.readline().split()]
        
        matches = [[]]
        for i in range(0, numM): 
            m = [int(i) for i in sys.stdin.readline().split()]
            matches.append(m)


        result = ""
        for team in range(1, n+1):
            teamWins = wins[team] 
            remainingMatches = 0
            net = [0]*(1+numM+n+1)
            net[0] = {}
            resi = [0]*(1+numM+n+1)
            resi[0] = {}
            for i in range(1, len(matches)):
                m = matches[i]
                if m[0] == team or m[1] == team:
                    teamWins += 1
                else:
                    remainingMatches += 1
                    #source -> match i
                    net[0][i] = 0
                    resi[0][i] = 1
                    #match i -> teams
                    net[i] = {numM + m[0]: 0, numM + m[1]:0}
                    resi[i] = {numM + m[0]: 1, numM + m[1]:1}
            
            for t in range(1, n+1):
                if t != team:
                    if teamWins - wins[t] < 0:
                        result += "no "
                        break
                    #team -> sink
                    net[numM+t] = {numM+n+1:0}
                    resi[numM+t] = {numM+n+1:teamWins - wins[t]}
            else:
                #print(team, net, resi)
                path = searchAugmentingPath(0, numM+n+1, resi)
                while path != -1:
                    cP = path[1]
                    path = path[0]
                    for i in range(0, len(path)-1):
                        u = path[i]
                        v = path[i+1]

                        #flow aument u -> v
                        if net[u].get(v, -1) != -1:
                            net[u][v] += cP
                            if resi[v] == 0:
                                resi[v] = {}
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
                    path = searchAugmentingPath(0, numM+n+1, resi)


                maxFlow = 0
                for v in net[0].keys():
                    maxFlow += net[0][v]
                if maxFlow == remainingMatches:
                    result += "yes "
                else:
                    result += "no "

                
        result = result[0:-1]
        
        print("Case #{0}: {1}".format(case, result))
        if case < case_count:
            input()
