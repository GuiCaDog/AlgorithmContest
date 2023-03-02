import sys
from queue import PriorityQueue





if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n, m = map(int, sys.stdin.readline().split())
        
        workers = PriorityQueue()
        tasks = []
        for i in range(0, n):
            ti = int(input()) 
            tasks.append(ti)
            
        tasks = sorted(tasks,reverse=True)
        
        for i in range(0, m):
            workers.put((0,i))
        time=0
        for t in tasks:
            w = workers.get()
            upW = w[0] + t
            time = max(time, upW)
            workers.put((upW,w[1]))
        
        print("Case #{0}: {1}".format(case, time))

        if case < case_count:
            input()
