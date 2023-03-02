import sys
from collections import deque 
import math

if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):

        n = int(input())
        

        tasks = [0]*(n+2)
        #########################################
        for i in range(0, len(tasks)):
            tasks[i] = {}
        for i in range(1, n+1):
            task = sys.stdin.readline().split()
            time = int(task[0])
            scors = [int(a) for a in task[2:]]
            for suc in scors:
                tasks[i][suc] = -time
            if i == n:
                tasks[n][n+1] = -time 


        dist = [100]*(n+2)
        dist[1] = 0 

        phase = deque([1])
        nextPhase = {}

        for nPhase in range(1, n+2):
            while len(phase) != 0:
                v = phase.popleft() 
                for w in tasks[v].keys():
                    if dist[v] + tasks[v][w] < dist[w]:
                        dist[w] = dist[v] + tasks[v][w]
                        nextPhase[w] = 1

            for key in nextPhase.keys():
                phase.append(key)
            nextPhase = {}

        x = dist[n+1] 


        
        print("Case #{0}: {1}".format(case, -x))

        if case < case_count:
            input()
