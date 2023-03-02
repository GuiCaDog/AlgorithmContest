import sys
from collections import deque



if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n = int(input())
        
        tasks = [0]*(n+2) 
        deQuiDepenc = {}
        for i in range(1, n+2):
            tasks[i] = {} 
            deQuiDepenc[i] = {} 
        for i in range(1, n+1):
            task = sys.stdin.readline().split()
            time = int(task[0])
            succ = [int(s) for s in task[2:]]
            for suc in succ:
                tasks[i][suc] = time
                deQuiDepenc[suc][i] = time
            if i == n:
                tasks[i][n+1] = time
                deQuiDepenc[n+1][i] = time

        #top_sorting
        dist = [10000] * (n+2)

        pre = [0] * (n+2)
        for v in deQuiDepenc.keys():
            pre[v] = len(deQuiDepenc[v])

        S = deque()
        i = 1
        for v in range(1, n+2):
            if pre[v] == 0:
                ###TSExplore
                if dist[v] == 10000:
                    S.append(v)
                while len(S) > 0:
                    ve = S.popleft()
                    dist[ve] = i
                    i+=1
                    for ad in tasks[ve].keys():
                        pre[ad] -= 1
                        if pre[ad] == 0:
                            S.append(ad)
        topSort = [0]*(n+2)
        for i in range(1, n+2):
            topSort[dist[i]] = i


        dist = [-10000] * (n+2)
        dist[1] = 0

        for i in range(1, n + 2):
            p = topSort[i]
            for s in tasks[p].keys():
                if tasks[p][s] + dist[p] > dist[s]:
                    dist[s] = tasks[p][s] + dist[p]

        

        print("Case #{0}: {1}".format(case, dist[n+1]))

        if case < case_count:
            input()
