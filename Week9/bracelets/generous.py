import sys

def lcs(a, b):

    matrix = [0]*(len(b)+1)
    for i in range(len(b)+1):
        matrix[i] = [0]*(len(a)+1)
    a="-"+a
    b="-"+b
    for row in range(1,len(b)):
        for col in range(1,len(a)):
            if a[col] == b[row]: #match
                matrix[row][col] = matrix[row-1][col-1] + 1
            else:
                matrix[row][col] = max(matrix[row-1][col], matrix[row][col-1])
    #for i in range(len(b)):
    #    print(i)
    #    print(matrix[i])
    return matrix[len(b)-1][len(a)-1]

def reverse(s):
    res = ""
    for i in range(len(s)-1, -1, -1):
        res+=(s[i])

    return res

def rotations(s):
    res = []
    for i in range(len(s)):
        res.append(s[i:] + s[:i])

    return res


if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        a = str(input()) 
        b = str(input()) 
        bestGift = 0
        if len(a) > len(b):
            rot = rotations(b)
            for r in rot:
                res1 = lcs(a,r)
                if res1 > bestGift:
                    bestGift = res1
                res2 = lcs(a,reverse(r))
                if res2 > bestGift:
                    bestGift = res2
        else:
            rot = rotations(a)
            for r in rot:
                res1 = lcs(b,r)
                if res1 > bestGift:
                    bestGift = res1
                res2 = lcs(b,reverse(r))
                if res2 > bestGift:
                    bestGift = res2
        

        
        print("Case #{0}: {1}".format(case, bestGift))

        if case < case_count:
            input()
