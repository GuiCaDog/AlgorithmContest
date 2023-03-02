import sys
import math
import random 

def dist_sq(p1, p2): 
    return math.sqrt((p1[0] - p2[0])*(p1[0]- p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1]))

def isRectangle(v1, v2, v3, v4):
    cx = (v1[0] + v2[0] + v3[0] + v4[0]) / 4
    cy = (v1[1] + v2[1] + v3[1] + v4[1]) / 4

    d1 = dist_sq(v1, (cx, cy))
    d2 = dist_sq(v2, (cx, cy))
    d3 = dist_sq(v3, (cx, cy))
    d4 = dist_sq(v4, (cx, cy))

    if abs(d1-d2) < 1e-6  and abs(d2-d3) < 1e-6 and abs(d3-d4) < 1e-6:
        return True
    else:
        return False

def getRectangleSides(v1, v2, v3, v4):
    sides = []
    d2 = dist_sq(v1, v2)
    d3 = dist_sq(v1, v3)
    d4 = dist_sq(v1, v4)
    order = []
    if d2 == max(d2, d3, d4):
        sides.append([v1[0],v1[1], v3[0],v3[1]])
        sides.append([v1[0],v1[1], v4[0],v4[1]])
        sides.append([v3[0],v3[1], v2[0],v2[1]])
        sides.append([v4[0],v4[1], v2[0],v2[1]])
        order = [v1, v3, v2, v4]
    elif d3 == max(d2, d3, d4):
        sides.append([v1[0],v1[1], v2[0],v2[1]])
        sides.append([v1[0],v1[1], v4[0],v4[1]])
        sides.append([v2[0],v2[1], v3[0],v3[1]])
        sides.append([v4[0],v4[1], v3[0],v3[1]])
        order = [v1, v2, v3, v4]
    else:
        sides.append([v1[0],v1[1], v2[0],v2[1]])
        sides.append([v1[0],v1[1], v3[0],v3[1]])
        sides.append([v2[0],v2[1], v4[0],v4[1]])
        sides.append([v3[0],v3[1], v4[0],v4[1]])
        order = [v1, v2, v4, v3]

    return sides, order


def within(p, q, r):
    return p <= q <= r or r <= q <= p

def isOnSeg(seg, p):
    ax,ay,bx,by = seg
    px,py = p
    #collinear = abs((py - ay)*(bx-ax) - (px-ax)*(by-ay)) < 1e-6
    if  within(ax,px,bx) and within(ay, py, by):
        return True
    else:
        return False


def doIntersect(seg1, seg2):
    ax, ay, bx, by = seg1
    cx, cy, dx, dy = seg2

    #They are parallel because they have same slope
    if abs((by - ay)*(dx-cx) - (bx-ax)*(dy-cy)) < 1e-6:
        return False
    else:
        px = ((bx-ax)*(cx*dy-dx*cy) - (dx - cx)*(ax*by-bx*ay)) / ((bx-ax)*(dy-cy) - (by-ay)*(dx-cx))
        py = ((by-ay)*(cx*dy-dx*cy) - (dy - cy)*(ax*by-bx*ay)) / ((bx-ax)*(dy-cy) - (by-ay)*(dx-cx))
        
        if isOnSeg(seg1, (px, py)) and isOnSeg(seg2, (px, py)):
            return True
        else:
            return False

def isPointInside(P, polygon):
    ax,ay = P
    badRay = True
    while badRay:
        count = 0
        bx, by = (2000, random.randint(-2000, 2000))
    
        for side in polygon:
            cx, cy, dx, dy = side
    
            #check that neither cx,cy nor dx,dy vertex are on the line
            if (cy-ay)*(bx-ax) == (cx-ax)*(by-ay) or (dy-ay)*(bx-ax) == (dx-ax)*(by-ay):
                #one of the vertex lies in the line (a,b),
                #cause the slope resulting from (a,b) is the same from (a,c) or (a,d)
                break
    
    
            #They are parallel because they have same slope
            if (by - ay)*(dx-cx) == (bx-ax)*(dy-cy):
                continue
    
    
            #get intersection from ray to side
            px = ((bx-ax)*(cx*dy-dx*cy) - (dx - cx)*(ax*by-bx*ay)) / ((bx-ax)*(dy-cy) - (by-ay)*(dx-cx))
    
            py = ((by-ay)*(cx*dy-dx*cy) - (dy - cy)*(ax*by-bx*ay)) / ((bx-ax)*(dy-cy) - (by-ay)*(dx-cx))
    
            if by <= ay:
                if px >= ax and py <= ay:
                    if (((px >= cx and px <= dx) or (px >= dx and px <= cx)) and
                        ((py >= cy and py <= dy) or (py >= dy and py <= cy))):
                        #if intersection x-coordinate lies between side (c,d)
                        count+=1
                        #print(px,py)
            elif by >= ay:
                if px >= ax and py >= ay:
                    if (((px >= cx and px <= dx) or (px >= dx and px <= cx)) and
                        ((py >= cy and py <= dy) or (py >= dy and py <= cy))):
                        #if intersection x-coordinate lies between side (c,d)
                        count+=1
    
        else:
            badRay = False
    
    
    if count % 2 == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n = int(input()) 
        
        vertices = []
        for i in range(0, n):
            vertex = sys.stdin.readline().split()
            vertex = (int(vertex[0]), int(vertex[1]))
            vertices.append(vertex)


        
        possible = False
        res = "impossible"
        goodVertices = []
        for r1 in range(len(vertices)):
            if possible:
                break
            v1 = vertices[r1]
            for r2 in range(r1+1, len(vertices)):
                if possible:
                    break
                v2 = vertices[r2]
                for r3 in range(r2+1, len(vertices)):
                    if possible:
                        break
                    v3 = vertices[r3]
                    for r4 in range(r3+1, len(vertices)):
                        if possible:
                            break
                        v4 = vertices[r4]
                        if not isRectangle(v1, v2, v3, v4):
                            continue
                        else:
                            rectSides, order = getRectangleSides(v1,v2,v3,v4)
                            #print(v1, v2, v3, v4)
                            #print(rectSides)
                            for r5 in range(len(vertices)):
                                if possible:
                                    break
                                if r5 == r1 or r5 == r2 or r5 == r3 or r5 == r4:
                                    continue
                                else:
                                    v5 = vertices[r5]
                                    for r6 in range(r5+1, len(vertices)):
                                        if possible:
                                            break
                                        if r6 == r1 or r6 == r2 or r6 == r3 or r6 == r4:
                                            continue
                                        else:
                                            v6 = vertices[r6]
                                            for r7 in range(r6+1, len(vertices)):
                                                if possible:
                                                    break
                                                if r7 == r1 or r7 == r2 or r7 == r3 or r7 == r4:
                                                    continue
                                                else:
                                                    v7 = vertices[r7]
                                                    trianSides = []
                                                    trianSides.append([v5[0],v5[1],v6[0],v6[1]])
                                                    trianSides.append([v5[0],v5[1],v7[0],v7[1]])
                                                    trianSides.append([v6[0],v6[1],v7[0],v7[1]])
                                                    #print(trianSides)
                                                    for i in range(3):
                                                        if (doIntersect(trianSides[i], rectSides[0]) or doIntersect(trianSides[i], rectSides[1]) 
                                                                or doIntersect(trianSides[i], rectSides[2]) or doIntersect(trianSides[i], rectSides[3])):
                                                            break
                                                    else:#good triangle so far, now check if a point is inside or outside
                                                        if (not isPointInside(v1, trianSides)) and (not isPointInside(v5, rectSides)):
                                                            possible = True
                                                            goodVertices = order
                                                            goodVertices += [v5,v6,v7]
                                                            #print(trianSides)
                                                            res = "possible"
                                                            #print("possibleeeeeeee!")
                                                        #else:
                                                        #    print(isPointInside(v1, trianSides))
                                                        #    print(trianSides)


        print("Case #{0}: {1}".format(case, res))
        if possible:
            for v in goodVertices:
                print(v[0],v[1])

        if case < case_count:
            input()
