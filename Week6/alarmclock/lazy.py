import sys

def printClockDigit(digit):
    if digit[0] == 1:
        print('|', end="")
    else:
        print(" ", end="")
    if digit[1] == 1:
        print('^', end="")
    else:
        print(" ", end="")
    if digit[2] == 1:
        print('|')
    else:
        print(" ")
    if digit[4] == 1:
        print('|', end="")
    else:
        print(' ', end="")
    if digit[3] == 1:
        print('^', end="")
    else:
        print(' ', end="")
    if digit[6] == 1:
        print('|')
    else:
        print(' ')
    if digit[5] == 1:
        print(' ^')
    else:
        print(' ')

def checkCompatibility(tiles1, tiles2):
    tiles1 = [intToClock[tiles1[0]],intToClock[tiles1[1]],intToClock[tiles1[2]], intToClock[tiles1[3]]]
    for i in range(0, 4):
        iTiles = tiles1[i]
        broke = False
        for j in range(0, 7):
            if iTiles[j] == 1:
                if tiles2[i][j] == 1 or tiles2[i][j] == 0:
                    pass
                else:
                    broke = True
                    break
            if iTiles[j] ==0:
                if tiles2[i][j] == 0 or tiles2[i][j] == 2:
                    pass
                else:
                    broke = True
                    break
        if broke:
            return False
    return True

if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n = int(input())

        intToClock = {1:[0,0,1,0,0,0,1], 2:[0,1,1,1,1,1,0], 
                      3:[0,1,1,1,0,1,1], 4:[1,0,1,1,0,0,1],
                      5:[1,1,0,1,0,1,1], 6:[1,1,0,1,1,1,1],
                      7:[0,1,1,0,0,0,1], 8:[1,1,1,1,1,1,1],
                      9:[1,1,1,1,0,1,1], 0:[1,1,1,0,1,1,1]}

        clockToInt = {"0010001":1, "0111110":2, 
                      "0111011":3, "1011001":4,
                      "1101011":5, "1101111":6,
                      "0110001":7, "1111111":8,
                      "1111011":9, "1110111":0}
        
        times = [0]*n
        for i in range(0, n):
            t = sys.stdin.readline()
            a = int(t[0])
            b = int(t[1])
            c = int(t[3])
            d = int(t[4])
            times[i] = [a,b,c,d]
        
        timesInTiles = [0]*n
        for i in range(0, n):
            timesInTiles[i] = [0]*4
            for j in range(0, 4):
                timesInTiles[i][j] = intToClock[times[i][j]]

        tilesAlive = [0]*4  
        for i in range(0, 4):
            tilesAlive[i] = [0]*7

        for i in range(0, n):
            for j in range(0, 4):
                for k in range(0, 7):
                    tilesAlive[j][k] += timesInTiles[i][j][k]

        for j in range(0, 4):
            for k in range(0, 7):
                tilesAlive[j][k] = min(1, tilesAlive[j][k]) 
        
        #alivesInDigits = [0]*4
        #for i in range(0, 4):
        #    tile = ""
        #    for j in tilesAlive[i]:
        #        tile =  tile + str(j)
        #    alivesInDigits[i] = clockToInt[tile]
        
        #0: it's off, but may be a broken tile
        #1: it's onn
        #2: it's off, but the tile is working on the clock
        #so we can only change tiles that has the 0 when searching other possible times
        firstOnOffTiles = [0]*n
        for k in range(0, n):
            firstOnOffTiles[k] = [0]*4
            for i in range(0, 4):
                firstOnOffTiles[k][i] = [0]*7
                for j in range(0, 7):
                    if timesInTiles[k][i][j] == 1:
                        firstOnOffTiles[k][i][j] = 1
                    if timesInTiles[k][i][j] == 0 and tilesAlive[i][j] == 1:
                        firstOnOffTiles[k][i][j] = 2


        posFirst1 = []        
        for i in range(0,3):
            iTiles = intToClock[i]
            for j in range(0, 7):
                if iTiles[j] == 1:
                    if firstOnOffTiles[0][0][j] == 1 or firstOnOffTiles[0][0][j] == 0:
                        pass
                    else:
                        break
                if iTiles[j] ==0:
                    if firstOnOffTiles[0][0][j] == 0 or firstOnOffTiles[0][0][j] == 2:
                        pass
                    else:
                        break
            else:
                posFirst1.append(i)

        posFirst2 = []        
        for i in range(0,10):
            iTiles = intToClock[i]
            for j in range(0, 7):
                if iTiles[j] == 1:
                    if firstOnOffTiles[0][1][j] == 1 or firstOnOffTiles[0][1][j] == 0:
                        pass
                    else:
                        break
                if iTiles[j] ==0:
                    if firstOnOffTiles[0][1][j] == 0 or firstOnOffTiles[0][1][j] == 2:
                        pass
                    else:
                        break
            else:
                posFirst2.append(i)

        posFirst3 = []        
        for i in range(0,6):
            iTiles = intToClock[i]
            for j in range(0, 7):
                if iTiles[j] == 1:
                    if firstOnOffTiles[0][2][j] == 1 or firstOnOffTiles[0][2][j] == 0:
                        pass
                    else:
                        break
                if iTiles[j] ==0:
                    if firstOnOffTiles[0][2][j] == 0 or firstOnOffTiles[0][2][j] == 2:
                        pass
                    else:
                        break
            else:
                posFirst3.append(i)

        posFirst4 = []        
        for i in range(0,10):
            iTiles = intToClock[i]
            for j in range(0, 7):
                if iTiles[j] == 1:
                    if firstOnOffTiles[0][3][j] == 1 or firstOnOffTiles[0][3][j] == 0:
                        pass
                    else:
                        break
                if iTiles[j] ==0:
                    if firstOnOffTiles[0][3][j] == 0 or firstOnOffTiles[0][3][j] == 2:
                        pass
                    else:
                        break
            else:
                posFirst4.append(i)



        print("Case #{0}:".format(case))
        one = 0
        for i in posFirst1:
            for j in posFirst2:
                for k in posFirst3:
                    for h in posFirst4:
                        if (i != 2 or (i==2 and j < 4)):
                            d=h
                            c=k
                            b=j
                            a=i
                            for t in range(1, n):
                                #calculate initial time + t
                                d += 1
                                if d == 10:
                                    d = 0
                                    c += 1
                                    if c == 6:
                                        c = 0
                                        b += 1
                                        if a == 0 and b == 10:
                                            a = 1
                                            b = 0
                                        elif i==1 and b == 10:
                                            a = 2
                                            b = 0
                                        elif i==2 and b==4:
                                            a = 0
                                            b = 0
                                #print([a,b,c,d])
                                if not checkCompatibility([a,b,c,d], firstOnOffTiles[t]):
                                    break
                            else:
                                one+=1
                                print("{0}{1}:{2}{3}".format(i,j,k,h))
        if one == 0:
            print("none")
        if case < case_count:
            input()
