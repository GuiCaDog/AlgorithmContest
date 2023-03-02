import sys

if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        s, f = map(int, sys.stdin.readline().split())
        
        stations = []
        rooms = []
        for i in range(0, s):
            sRooms = sys.stdin.readline().split()
            sRooms = [int(i) for i in sRooms]
            stations.append(sRooms)
            
        stations = sorted(stations, key=lambda x: x[0])

        for j in range(0, len(stations)):
            while stations[j][0] <= stations[j][1]:
                for i in range (j, len(stations)):
                    if i == j: #station at the top

                        if j < len(stations) -1:
                            while stations[j][0] <= stations[j+1][0]:
                                rooms.append((stations[i][0]))
                                stations[j][0] += 1

                        else:
                            while stations[j][0] <= stations[j][1]:
                                rooms.append(stations[j][0])
                                stations[j][0]+=1



                    elif stations[i][0] == stations[j][0]-1 and stations[i][0] <= stations[i][1]: 
                        rooms.append((stations[i][0]))
                        stations[i][0] += 1
                        #if stations[i][0] == stations[i][1]:
                        #    rooms.append((stations[i][0]))

        print("Case #{0}:".format(case))
        for i in range(0, f):
            lineNum = int(input())
            print(rooms[lineNum-1])



        if case < case_count:
            input()
