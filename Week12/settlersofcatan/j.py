import sys

def step(inArray, board):
    outArray = [-1]*(len(inArray) + 6)
    window = len(inArray) // 6
    j = 0
    for i in range(0, len(outArray)):
        if window > 0:
            outArray[i] = inArray[j-1] + inArray[j]
            j+=1
            window-=1
        else:
            outArray[i] = inArray[j-1]
            window = len(inArray) // 6
    
    return outArray

def lowest(board):
    m = 100000 
    n = -1
    for i in range(len(board)):
        if board[i] < m:
            m = board[i]
            n = i+1

    return n 



if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        q = int(input())
        base = [-1, 1,2,3,4,5,2,3]
        if q <= 7:
            print("Case #{0}: {1}".format(case, base[q]))
        else:
            res = -2
            board = [1, 2, 2, 1, 1]
            n = 7
            inArray = [2,3,4,5,2,3]

            while n < q:
                outArray = [-1]*(len(inArray) + 6)
                window = len(inArray) // 6
                j = 0
                for i in range(0, len(outArray)):
                    n+=1
                    if window > 0:
                        no1 = inArray[j-1] - 1
                        no2 = inArray[j] - 1
                        if i == 0:
                            no3 = inArray[-1] - 1
                        else:
                            no3 = outArray[i-1] - 1
                        if n == q:
                            print(no1, no2, no3)
                        k1 = board[no1] 
                        k2 = board[no2] 
                        k3 = board[no3] 
                        board[no1] = 1000000
                        board[no2] = 1000000
                        board[no3] = 1000000
                        outArray[i] = lowest(board) 
                        board[no1] = k1 
                        board[no2] = k2 
                        board[no3] = k3 
                        board[outArray[i]-1] += 1
                        
                        j+=1
                        window-=1

                    else:

                        no1 = inArray[j-1] - 1
                        no2 = outArray[i-1] - 1
                        if n == q:
                            print(no1, no2)
                        k1 = board[no1] 
                        k2 = board[no2] 
                        board[no1] = 1000000
                        board[no2] = 1000000
                        outArray[i] = lowest(board) 
                        board[no1] = k1 
                        board[no2] = k2 
                        board[outArray[i]-1] += 1
                        window = len(inArray) // 6
                    

                    if n == q:
                        res = outArray[i]
                        #break

                inArray = outArray


            print("Case #{0}: {1}".format(case, res))
            print(board)
            print(outArray)



