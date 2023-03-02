import sys
import heapq




if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n, m = map(int, sys.stdin.readline().split())
        
        workers = []
        tasks = []
        for i in range(0, n):
            ti = int(input()) 
            tasks.append(ti)
            
        tasks = sorted(tasks,reverse=True)
        
        for i in range(0, m):
            heapq.heappush(workers, (0,i))
        time=0
        for t in tasks:
            w = heapq.heappop(workers)
            upW = w[0] + t
            time = max(time, upW)
            heapq.heappush(workers, (upW,w[1]))
        
        print("Case #{0}: {1}".format(case, time))

        if case < case_count:
            input()
