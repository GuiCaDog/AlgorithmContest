import sys
from collections import deque

def searchAugmentingPath(s, t, resG):
        exploring = deque()
        exploring.append(s)

        pred = [0]*(len(resG)) 
        visited = [0]*(len(resG)) 

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
            pre = t
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
        n, k, d = map(int, sys.stdin.readline().split())
        
        #initializing arena
        mountains = [0] * (1+n*n)
        net = [0]*(n*n*(d+1)*2+2)
        resi = [0]*(n*n*(d+1)*2+2)
        #transforming map matrix into array
        for i in range(0, n):
            r = sys.stdin.readline().split()
            for j in range(0, n):
                mountains[1+i*n + j] = int(r[j]) 

        #initializing riders
        net[0] = {}
        resi[0] = {}
        for i in range(0, k):
            r, c = map(int, sys.stdin.readline().split())
            a = (r-1)*n+c
            net[0][a] = 0
            resi[0][a] = 1
            net[a] = {}
            resi[a] = {}


        for i in range(0, d+1):
            if i < d:
                snow = int(input())
            #we loop through matrix i
            iniMi = 2*n*n*i+1
            fiMi = iniMi + n*n
            for j in range(iniMi, fiMi):

                
                #someone can arrive here
                if net[j] != 0:
                    #only one can stay in this place
                    net[j][j+n*n] = 0
                    resi[j][j+n*n] = 1
                    net[j+n*n] = {}
                    resi[j+n*n] = {}

                    if i < d: #only if we are not in the last day

                        #now we check, to which positions you can go in day+1
                        stay = j + 2*n*n
                        north = j + 2*n*n - n
                        right = j + 2*n*n + 1
                        south = j + 2*n*n + n
                        left = j + 2*n*n -1

                        # we check that we're still in the map if we go north
                        if north > (i+1)*2*n*n: #this indicates the end of the day i

                            #we want to check if that position is free of snow
                            if mountains[north - (i+1)*2*n*n] > snow: #then we can survive there
                                if net[j+n*n] == 0:
                                    net[j+n*n] = {}
                                    resi[j+n*n] = {}
                                if net[north] == 0:
                                    net[north] = {}
                                    resi[north] = {}
                                net[j+n*n][north] = 0
                                resi[j+n*n][north] = 1


                        
                        # we check that we're still in the map if we go right
                        #this indicates the end of the day i+1 
                        if right <= (i+2)*2*n*n - n*n and (j - i*2*n*n) % n != 0: 
                            
                            originalPos = right - (i+1)*2*n*n
                            #we want to check if that position is free of snow
                            if mountains[originalPos] > snow: #then we can survive there
                                if net[j+n*n] == 0:
                                    net[j+n*n] = {}
                                    resi[j+n*n] = {}
                                if net[right] == 0:
                                    net[right] = {}
                                    resi[right] = {}
                                net[j+n*n][right] = 0
                                resi[j+n*n][right] = 1

                        # we check that we're still in the map if we go south
                        if south <= (i+2)*2*n*n - n*n: #this indicates the end of the day i+1

                            #we want to check if that position is free of snow
                            if mountains[south - (i+1)*2*n*n] > snow: #then we can survive there
                                if net[j+n*n] == 0:
                                    net[j+n*n] = {}
                                    resi[j+n*n] = {}
                                if net[south] == 0:
                                    net[south] = {}
                                    resi[south] = {}
                                net[j+n*n][south] = 0
                                resi[j+n*n][south] = 1

                        # we check that we're still in the map if we go left
                        if left > (i+1)*2*n*n and (j -i*2*n*n) % n != 1: #this indicates the end of the day i

                            #we want to check if that position is free of snow
                            if mountains[left- (i+1)*2*n*n] > snow: #then we can survive there
                                if net[j+n*n] == 0:
                                    net[j+n*n] = {}
                                    resi[j+n*n] = {}
                                if net[left] == 0:
                                    net[left] = {}
                                    resi[left] = {}
                                net[j+n*n][left] = 0
                                resi[j+n*n][left] = 1

                        # we also have to consider if we can stay in our position
                        if mountains[stay - (i+1)*2*n*n] > snow:
                            if net[j+n*n] == 0:
                                net[j+n*n] = {}
                                resi[j+n*n] = {}
                            if net[stay] == 0:
                                net[stay] = {}
                                resi[stay] = {}
                            net[j+n*n][stay] = 0
                            resi[j+n*n][stay] = 1


                    else: # if it's the last day
                        net[j+n*n] = {2*n*n*(d+1)+1:0}
                        resi[j+n*n] = {2*n*n*(d+1)+1:1}
        #print(net)


                        

        path = searchAugmentingPath(0, len(net)-1, resi)
        while path != -1:
            cP = path[1]
            path = path[0]
            for i in range(0, len(path)-1):
                a = path[i]
                b = path[i+1]

                #flow aument a -> b
                if net[a].get(b, -1) != -1:
                    net[a][b] += cP
                    if resi[b] == 0:
                        resi[b] = {}
                    #resi[b][a] = resi[b].get(a,0) + net[a][b]
                    resi[b][a] =  net[a][b]
                    resi[a][b] -= cP
                #flow b -> a diminish
                else:
                    net[b][a] -= cP
                    #if there is less flow b -> a
                    #a -> b you've got less capacity
                    resi[a][b] -= cP
                    #you've got more capacity b -> a now
                    resi[b][a] += cP
            path = searchAugmentingPath(0, len(net)-1, resi)


        #print(net)
        maxFlow = 0
        for b in net[0].keys():
            maxFlow += net[0][b]
        
        print("Case #{0}: {1}".format(case, maxFlow))

        if case < case_count:
            input()
