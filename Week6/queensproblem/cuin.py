import sys


def doThePainting(board, queens, n):
    nQ = 0
    #check if we're done and search the next queen
    for q in range(0, n):
        if queens[q] == 0:
            nQ = q
            break
    else:
        return board 

    #check if we can place a queen
    for j in range(0, len(board[nQ])):
        if board[j][nQ] == 0:
            break
    else:
        return -1

    for j in range(0, n):
        if board[j][nQ] == 0:
            qAux = [i for i in queens]
            bAux = [0]*n
            for k in range(0, n):
                bAux[k] = [i for i in board[k]]
            bAux =  addQueen(qAux, bAux, j, nQ, n)
            res = doThePainting(bAux, qAux,n)
            if res != -1:
                return res

    return -1
    




def addQueen(queens, board, r, c, n):

    queens[c] = -1
    board[r][c] = 2 
    #paint row
    for i in range(0, n):
        board[r][i] = max(board[r][i], 1)

    #paint coulmn 
    for i in range(0, n):
        board[i][c] = max(board[i][c], 1)

    #paint main diag
    i = max(0, r-c)
    j = max(0, c-r)
    while i < n and j < n:
        board[i][j] = max(board[i][j], 1)
        i+=1
        j+=1

    #paint second diag
    i = min(n-1, r+c)
    j = max(0, c-(n-1-r))
    while i >= 0 and j < n:
        board[i][j] = max(board[i][j], 1)
        i-=1
        j+=1

    return board

def printBoard(board):
    if board == -1:
        print("impossible")
    else:
        for i in range(0, len(board)):
            for j in range(0, len(board)):
                if board[i][j] == 2:
                    print("x", end = "")
                else:
                    print(".", end = "")
            print("")



if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n = int(input())
        
        queens = [0]*n
        board = [0]* n
        for i in range(0, n):
            board[i] = [0]*n
        result = "" 
        for i in range(0, n):
            row = sys.stdin.readline()
            for j in range(0, n):
                if row[j] == 'x' and result != "impossible":
                    if board[i][j] == 1:
                        result = "impossible"
                        break
                    else:
                        addQueen(queens, board, i, j, n)
                    

        print("Case #{0}:".format(case))
        if result == "impossible":
            print(result)
        else:
            printBoard(doThePainting(board, queens, n))

        if case < case_count:
            input()
