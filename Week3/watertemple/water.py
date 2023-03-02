import sys
from collections import deque


if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n, m, k, l = map(int, sys.stdin.readline().split())
        
        hallWays = []
        blackTemple = {}

        for i in range(0, m):
            hWay = sys.stdin.readline().split()
            hWay = [int(hWay[0]), int(hWay[1]), int(hWay[2])]
            hallWays.append(hWay)
            
        hallWays = sorted(hallWays, key=lambda x: x[2], reverse=True)


        #Building our graf with accessible hallways at water level l
        acWayIndx = 0
        while acWayIndx < len(hallWays) and hallWays[acWayIndx][2] >= l:
            u = hallWays[acWayIndx][0]
            v = hallWays[acWayIndx][1]
            blackTemple[u] = blackTemple.get(u,[])
            blackTemple[u].append(v)
            blackTemple[v] = blackTemple.get(v,[])
            blackTemple[v].append(u)
            acWayIndx += 1

        #Building our map of control rooms
        cRooms = [-1]*(n+1) #{}
        for i in range(0, k):
            cR = sys.stdin.readline().split()
            cRooms[int(cR[0])] = int(cR[1])


        #Getting the accessible rooms in initial level
        accRoomsMap = [0]*(n+1)
        accRoomsMap[1] = 1
        accRooms = {1:1} #1 #can we just have a count?
        acCtrolRs = []
        #the minor level of water that we can achieve right now
        mWatLev = l
        if cRooms[1] != -1:
            acCtrolRs.append(1)
            if cRooms[1] < mWatLev:
                mWatLev = cRooms[1]

        exploring = deque()
        exploring.append(1)
        visited = [0]*(n+1)

        while len(exploring) != 0:
            exp = exploring.pop()
            visited[exp] = 1

            for room in blackTemple.get(exp,[]):
                if visited[room] != 1:

                    if cRooms[room] != -1: #if it's a control room
                        acCtrolRs.append(room)
                        #we update the level of water that we can achieve
                        if cRooms[room] < mWatLev:
                            mWatLev = cRooms[room]
                    
                    accRoomsMap[room] = 1
                    accRooms[room] = 1
                    exploring.append(room)

        #decreasing the water level gradually
        #let's see if we can reach all rooms
        
        #while we don't reach n rooms, but we can lower the water level 
        while len(list(accRooms.keys())) < n and l > mWatLev:
            l -= 1
            #we want to store the rooms that are in touch with 
            #the new accessible hallways, and we will make them unvisited
            #because we want to expand them again
            inTouch = {}

            #add new hallways to the black temple
            while acWayIndx < len(hallWays) and hallWays[acWayIndx][2] >= l:
                u = hallWays[acWayIndx][0]
                v = hallWays[acWayIndx][1]
                #------------------
                if accRoomsMap[u] == 1:
                    inTouch[u] = 1 
                if accRoomsMap[v] == 1:
                    inTouch[v] = 1
                visited[u] = 0
                visited[v] = 0
                #------------------
                blackTemple[u] = blackTemple.get(u,[])
                blackTemple[u].append(v)
                blackTemple[v] = blackTemple.get(v,[])
                blackTemple[v].append(u)
                acWayIndx += 1

            #now we want to explore again
            for room in inTouch:
                if visited[room] != 1:
                    exploring.append(room)
                while len(exploring) != 0:
                    exp = exploring.pop()
                    visited[exp] = 1

                    for room in blackTemple.get(exp,[]):
                        if visited[room] != 1:

                            if cRooms[room] != -1: #if it's a control room
                                acCtrolRs.append(room)
                                #we update the level of water that we can achieve
                                if cRooms[room] < mWatLev:
                                    mWatLev = cRooms[room]
                            
                            accRoomsMap[room] = 1
                            accRooms[room] = 1
                            exploring.append(room)
        
        result = "impossible"
        if len(list(accRooms.keys())) == n:
            result = l


        
        print("Case #{0}: {1}".format(case, result))

        if case < case_count:
            input()
