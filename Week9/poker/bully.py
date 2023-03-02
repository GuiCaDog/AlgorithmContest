import sys
#stations = sorted(stations, key=lambda x: x[0])

if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        
        n = int(input())
        
        #bestUpToDay = 
        tours = {}
        lastDay = 0
        for i in range(0, n):
            abc = sys.stdin.readline().split()
            abc = [int(abc[0]), int(abc[1]), int(abc[2])]
            tours[abc[1]] = tours.get(abc[1],[])
            tours[abc[1]].append(abc)
            if abc[1] > lastDay:
                lastDay = abc[1]
        
        bestUpToDay = [0]*(lastDay + 1)

        for day in range(1, len(bestUpToDay)):
            if tours.get(day, -1) == -1:#No new tournaments
                bestUpToDay[day] = bestUpToDay[day-1]
            else:
                bestPrize = 0 
                for tour in tours[day]:
                    if tour[2] + bestUpToDay[tour[0]-1] > bestPrize:
                        bestPrize = tour[2] + bestUpToDay[tour[0]-1]

                bestUpToDay[day] = max(bestPrize, bestUpToDay[day-1])
        
        print("Case #{0}: {1}".format(case, bestUpToDay[lastDay]))

        if case < case_count:
            input()
