import sys


def getTools(cave, currentTools, totalTools, w, h, i, j):
    if cave[i][j] == 7:
        currentTools += 1
    #check if we already have all the tools
    if currentTools == totalTools:
        return "yes"

    #check if we can make a step in any direction
    up = -1
    if i - 1 >= 0:
        up = cave[i-1][j]
    ri = -1
    if j + 1 < w:
        ri = cave[i][j+1]
    do  = -1
    if i + 1 < h:
        do = cave[i+1][j]
    le  = -1
    if j - 1 >= 0:
        le = cave[i][j-1]

    if up==0 or ri==0 or do==0 or le==0 or up==7 or ri==7 or do==7 or le==7:
        pass
    else:
        #no possible step
        return "no"
    
    #we can make a step up
    if up==0 or up==7:
        cAux = [0]*h
        for k in range(0, h):
            cAux[k] = [m for m in cave[k]]
        #paint our previous field
        cAux[i][j] = -2
        if getTools(cAux, currentTools, totalTools, w, h, i-1, j) == "yes":
            return "yes"
    
    #we can make a step right
    if ri==0 or ri==7:
        cAux = [0]*h
        for k in range(0, h):
            cAux[k] = [m for m in cave[k]]
        #paint our previous field
        cAux[i][j] = -2
        if getTools(cAux, currentTools, totalTools, w, h, i, j+1) == "yes":
            return "yes"
    
    #we can make a step down
    if do==0 or do==7:
        cAux = [0]*h
        for k in range(0, h):
            cAux[k] = [m for m in cave[k]]
        #paint our previous field
        cAux[i][j] = -2
        if getTools(cAux, currentTools, totalTools, w, h, i+1, j) == "yes":
            return "yes"

    #we can make a step le 
    if le==0 or le==7:
        cAux = [0]*h
        for k in range(0, h):
            cAux[k] = [m for m in cave[k]]
        #paint our previous field
        cAux[i][j] = -2
        if getTools(cAux, currentTools, totalTools, w, h, i, j-1) == "yes":
            return "yes"

    return "no"


def printBoard(board):
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            switch = {4:'#', 0:'_',7:'T',1:'L'}
            print(switch[board[i][j]], end = "")
        print("")

    #for i in range(0, len(board)):
    #    for j in range(0, len(board)):
    #        switch = {4:'#', 0:'_',7:'T',1:'L'}
    #        print(board[i][j], end = "")
    #    print("")



if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        w, h = map(int, sys.stdin.readline().split())

        tools = 0 
        cave = [0]* h
        li= lj = 0
        for i in range(0, h):
            cave[i] = [0]*w
        for i in range(0, h):
            row = sys.stdin.readline()
            for j in range(0, w):
                if row[j] == 'T':
                    tools += 1
                if row[j] == 'L':
                    li = i
                    lj = j
                switch = {'#':4, '_':0,'T':7,'L':1}
                cave[i][j] = switch[row[j]]
        
        yesNo = getTools(cave, 0, tools, w, h, li, lj) 
        print("Case #{0}: {1}".format(case, yesNo))

        if case < case_count:
            input()
