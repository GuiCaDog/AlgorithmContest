import sys



if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        s, f = map(int, sys.stdin.readline().split())
        
        stations = []
        rooms = []
        for i in range(0, s):
            sRooms = sys.stdin.readline().split()
            sRooms = [int(sRooms[0]), int(sRooms[1])]
            stations.append(sRooms)
            
        stations = sorted(stations, key=lambda x: x[0])

        #print(stations)
        
        print("Case #{0}:".format(case))
        for i in range(0, f):
            lineNum = int(input())
            

            ini = 1
            end = pow(2, 31) - 1 
            m = (ini + end) // 2
            stop = 0

            while stop == 0:
                #print(ini, end)
                #number of room numbers minor than m
                nMinorM = 0
                j = 0
                u = stations[j][0]
                v = stations[j][1]
                countMms = 0
                while j < len(stations) and u <= m:
                    #print(str(m) + " "+str(ini)+ " " +str(end))
                    #print(stations[j][0], stations[j][1])
                    try:
                        if m <= v:
                            nMinorM += ((m-1)-u + 1)
                            countMms += 1
                        else: #m > v
                            nMinorM += ((v-u) + 1)

                        if nMinorM >= lineNum:
                            #there are more rooms than lineNum before m, 
                            #m is in [1, n/2-1]
                            end = m-1
                            m = (ini + end) // 2
                            break
                        #if nMinorM == lineNum:
                            #we know that before m, there are nMinorM rooms
                            #but we don't know the number of the room prior to m
                            #because not every room number has to exists
                        
                    except:
                        #m is too large, because there are more than
                        #lineNum rooms before m
                        end = m-1
                        m = (ini + end) // 2
                        break

                    j+=1
                    if j < len(stations):
                        u = stations[j][0]
                        v = stations[j][1]

                #if nMinorM == lineNum - 1:
                #    #if previous to m, there are exactly lineNum - 1
                #    #rooms, at lineNum, there has to be m
                #    stop = 1
                #    print(m)

                if nMinorM < lineNum: 
                    #before m, there are nMinorM, and are less than lineNum
                    #so let's check, how many m are there
                    if nMinorM + countMms >= lineNum:
                        stop = 1
                        print(m)
                    else:
                    #before m, are nMinorM. There are countMms m after this,
                    #but they don't reach lineNum, so
                    #m is in [n/2+1, n]
                        ini = m + 1
                        m = (ini + end) // 2

        if case < case_count:
            input()
