import sys
import math
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
        
        vertices = []
        sides = []
        for i in range(0, n):
            vertex = sys.stdin.readline().split()
            vertex = (float(vertex[0]), float(vertex[1]), i)
            vertices.append(vertex)
            if i > 0:
                sides.append([vertices[i-1], vertex])

        sides.append([vertices[n-1],vertices[0]])


#---------------Centroid Calculation--------------------------------
        A = 0
        sumOfTheA = 0
        for i in range(len(vertices)):
            v1 = vertices[i]
            if i == len(vertices)-1:
                v2 = vertices[0] 
            else:
                v2 = vertices[i+1]

            sumOfTheA +=(v1[0]*v2[1] - v2[0]*v1[1])

        A = sumOfTheA / 2
        
        sumX = 0
        for i in range(len(vertices)):
            v1 = vertices[i]
            if i == len(vertices)-1:
                v2 = vertices[0] 
            else:
                v2 = vertices[i+1]

            sumX += ((v1[0]+v2[0])*(v1[0]*v2[1]-v2[0]*v1[1]))
        
        CX = sumX / (6*A)

        sumY = 0
        for i in range(len(vertices)):
            v1 = vertices[i]
            if i == len(vertices)-1:
                v2 = vertices[0] 
            else:
                v2 = vertices[i+1]

            sumY += ((v1[1]+v2[1])*(v1[0]*v2[1]-v2[0]*v1[1]))
        
        CY = sumY / (6*A)

#-----------------Getting Convex Hull of vertices -------------------------------------------------------------------------------------------------
        pMin = getPmin(vertices)
        
        #------------sort by angle without pMin--------------
        vertices = sorted(vertices[:pMin[2]] + vertices[(pMin[2]+1):], key=functools.cmp_to_key(lambda p1, p2:polar_comparator(p1,p2, pMin)))
        


        #-----------add pMin to Q ---------------------------
        vertices= [pMin] + vertices
        

        #-----------start stack -----------------------------
        H = [-1]*(n+1)
        H[1] = vertices[0]
        H[2] = vertices[1]
        h = 2
        
        #---------------iterate over Q-----------------------
        for i in range(2, len(vertices)):
            qi = vertices[i]
            while CCW(H[h-1], H[h], qi) >= 0:
                h-=1
                #only pMin in the stack, then push qi
                if h == 1:
                    break
            
            H[h+1] = qi
            h+=1
        
        
        #------get vertex that form part of the convex hull------------
        convexHull = {} 
        for i in range(len(H)):
            e = H[i]
            if e != -1 and i <= h:
                convexHull[e[2]] = 1
    
#---------------------------------------------------------------------------------------------------------------------
        #Recover possible sides
        goodSides = []
        for side in sides:
            v1 = side[0]
            v2 = side[1]
            if convexHull.get(v1[2], -1) != -1 and convexHull.get(v2[2], -1) != -1:
                goodSides.append(side)
        
        #Get perpendicular line to the segment, passing through middle of the segment 
        goodCount = 0
        for side in goodSides:
            x1,y1,*_ = side[0]
            x2,y2,*_ = side[1]
            mx,my = [(x1+x2) / 2, (y1+y2) / 2]  
            if (y2-y1) == 0:
                bx = mx
                by = my + 1
            else:
                perpSlope = (x1-x2)/(y2-y1)
                
                bx = mx + 1 
                by = perpSlope*(bx-mx) + my

            #(m, b) define a perpendicular line to side
            #print(side)
            #print(mx,my, bx, by)
            
            #Get distance from center of mass to that perpendicular line
            d = abs((bx - mx)*(my - CY) - (mx - CX)*(by-my)) / math.sqrt(pow((bx-mx),2) + pow((by-my),2))

            if d <= math.sqrt(dist_sq((mx, my), (x1, y1))):
                goodCount += 1

            


        print("Case #{0}:".format(case))
        #print(convexHull)
        ##print(sides)
        #print(goodSides)
        #print(A)
        #print(CX, CY)
        print(goodCount)


        if case < case_count:
            input()
