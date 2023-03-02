import sys

def buildPattern(pattern, tiles, k, i, j):
    #we need to check if we have a block above, at our left,
    leftTile  = -1
    leftColor = -2
    if j > 0: 
        leftTile = pattern[i][j-1]
        leftColor = tiles[leftTile][1]

    upTile= -1
    upColor= -2
    if i > 0: 
        upTile= pattern[i-1][j]
        upColor= tiles[upTile][2]

    #also if we are at the right edge, check element of the left edge
    riTile = -1
    riCol = -2
    if j == k-1:
        riTile = pattern[i][0]
        riCol = tiles[riTile][3]

    #if we are at the bottom, check element of the top
    doTile = -1
    doCol = -2
    if i == k-1:
        doTile = pattern[0][j]
        doCol = tiles[doTile][0]
    
    for t in range(0, len(tiles)):
        tile = tiles[t]
        if ((leftColor==-2 or leftColor==tile[3]) and
            (upColor==-2 or upColor==tile[0]) and
            (riCol==-2 or riCol==tile[1]) and
            (doCol==-2 or doCol==tile[2])):

            if i == k-1 and j == k-1:
                pattern[i][j] = t
                return pattern

            pAux = [0]*k
            for m in range(0, k):
                pAux[m] = [h for h in pattern[m]]
            pAux[i][j] = t

            if j==k-1:
                res = buildPattern(pAux, tiles, k, i+1, 0) 
                if res != -1:
                    return res
            else:
                res = buildPattern(pAux, tiles, k, i, j+1)
                if res != -1:
                    return res 
    return -1

def printBoard(board):
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            #switch = {4:'#', 0:'_',7:'T',1:'L'}
            if j == len(board[0]) - 1:
                print(board[i][j])
            else:
                print(board[i][j], end = " ")

    #for i in range(0, len(board)):
    #    for j in range(0, len(board)):
    #        switch = {4:'#', 0:'_',7:'T',1:'L'}
    #        print(board[i][j], end = "")
    #    print("")



if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n = int(input())
        
        tiles = [0]* n

        for i in range(0, n):
            tiles[i] = [int(j) for j in sys.stdin.readline().split()]
        

        k = 2
        res = -1 
        while k <= 20:

            pattern = [0]*k
            for i in range(0, k):
                pattern[i] = [-1]*k

            res = buildPattern(pattern, tiles, k, 0, 0)
            #if res != -1:
            #    break
            k+=1
        if res != -1:
            print("Case #{0}: {1}".format(case, k))
            printBoard(res)
        else:
            print("Case #{0}: {1}".format(case, "impossible"))

        if case < case_count:
            input()
