import sys



if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        s, f = map(int, sys.stdin.readline().split())
        
        stations = []
        for i in range(0, s):
            sRooms = sys.stdin.readline().split()
            sRooms = [int(sRooms[0]), int(sRooms[1])]
            stations.append(sRooms)
            
        stations = sorted(stations, key=lambda x: x[0])
        
        print("Case #{0}:".format(case))

        if case < case_count:
            input()
