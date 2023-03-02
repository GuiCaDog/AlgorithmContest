import sys
from collections import deque
import functools

def getPmin(points):
    px = 2000
    py = 2000
    minI = -1
    for p in points:
        if p[0] < px:
            px = p[0]
            py = p[1]
            minI = p[2]
        elif p[0] == px and p[1] < py:
            py = p[1]
            minI = p[2]

    return (px, py, minI)

def CCW(a,b,p):
    ax,ay,*_  = a
    bx,by,*_  = b
    px,py,*_  = p
    return (py-ay)*(bx-ax) - (px-ax)*(by-ay)

def dist_sq(p1, p2): 
    return (p1[0] - p2[0])*(p1[0]- p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1]) 

def polar_comparator(p1, p2, p0):
    d = CCW(p0, p1, p2)
    if d < 0:
        return -1
    if d > 0:
        return 1
    if d == 0:
        if dist_sq(p1, p0) < dist_sq(p2, p0):
            return -1
        else:
            return 1



if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n = int(input()) 
        
        fences = []
        for i in range(1, n+1):
            fence = sys.stdin.readline().split()
            fence = (int(fence[0]), int(fence[1]), i)
            fences.append(fence)

        pMin = getPmin(fences)
        
        #------------sort by angle without pMin--------------
        fences = sorted(fences[:(pMin[2]-1)] + fences[pMin[2]:], key=functools.cmp_to_key(lambda p1, p2:polar_comparator(p1,p2, pMin)))
        

        #------------remove collinears to pMin---------------
        #to_remove = []
        #for i in range(len(fences) - 1):
        #    d = CCW(fences[i], fences[i + 1], pMin)
        #    if d == 0:
        #        to_remove.append(i)
        #fences= [i for j, i in enumerate(fences) if j not in to_remove]
        #----------------------------------------------------


        #-----------add pMin to Q ---------------------------
        fences = [pMin] + fences
        

        #-----------start stack -----------------------------
        H = [-1]*(n+1)
        H[1] = fences[0]
        H[2] = fences[1]
        h = 2
        
        #---------------iterate over Q-----------------------
        for i in range(2, len(fences)):
            qi = fences[i]
            while CCW(H[h-1], H[h], qi) >= 0:
                h-=1
                #only pMin in the stack, then push qi
                if h == 1:
                    break
            
            H[h+1] = qi
            h+=1
        
        
        #------get and sort result---------------------------
        res = []
        for i in range(len(H)):
            e = H[i]
            if e != -1 and i <= h:
                res.append(e[2])
        res.sort()
    
        print("Case #{0}:".format(case), end=" ")
        for i in res:
            print(i, end=" ")
        print()


        if case < case_count:
            input()
