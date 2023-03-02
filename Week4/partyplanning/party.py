import sys



if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n = int(input())
        
        tasks = {} 
        tasksCost = [0]*(n+1)
        deQuiDepenc = {}
        for i in range(1, n+1):
            deQuiDepenc[i] = {} 
        for i in range(1, n+1):
            task = sys.stdin.readline().split()
            succ = [int(s) for s in task[2:]]
            nTask = i
            costTask = int(task[0])
            tasksCost[nTask] = costTask
            tasks[nTask] = succ 
            for suc in succ:
                deQuiDepenc[suc][nTask] = 1
        

        #print(deQuiDepenc)
        time = tasksCost[1] 
        tasksDone = [1]
        deQuiDepenc.pop(1, None)
        for t in list(deQuiDepenc.keys()):
            deQuiDepenc[t].pop(1, None)
        #print(deQuiDepenc)
        while len(tasksDone) != n:
            nextTasks = []
            maxNextTask = 0
            for t in list(deQuiDepenc.keys()):
                if len(deQuiDepenc[t]) == 0:
                    if tasksCost[t] > maxNextTask:
                        maxNextTask = tasksCost[t]
                    nextTasks.append(t)
                    tasksDone.append(t)
                    deQuiDepenc.pop(t, None)
                    

            time += maxNextTask
            for t in nextTasks:
                for ta in list(deQuiDepenc.keys()):
                    deQuiDepenc[ta].pop(t, None)
        #    print(deQuiDepenc)
            
        
        print("Case #{0}: {1}".format(case, time))

        if case < case_count:
            input()
