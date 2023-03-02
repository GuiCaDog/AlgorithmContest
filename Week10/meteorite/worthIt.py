import sys
import random 



if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        ax, ay, n = map(int, sys.stdin.readline().split())
        
        sides = []
        for i in range(0, n):
            side = sys.stdin.readline().split()
            side = [int(side[0]), int(side[1]), int(side[2]), int(side[3])]
            sides.append(side)

        badRay = True 
        while badRay:
            count = 0
            bx, by = (2000, random.randint(-2000, 2000)) 

            for side in sides:
                cx, cy, dx, dy = side

                #check that neither cx,cy nor dx,dy vertex are on the line
                if (cy-ay)*(bx-ax) == (cx-ax)*(by-ay) or (dy-ay)*(bx-ax) == (dx-ax)*(by-ay):
                    #one of the vertex lies in the line (a,b), 
                    #cause the slope resulting from (a,b) is the same from (a,c) or (a,d) 
                    print("caca")
                    break

                
                #if by <= ay:
                #    if min(cy, dy) > ay:
                #        continue
                #They are parallel because they have same slope
                if (by - ay)*(dx-cx) == (bx-ax)*(dy-cy):
                    print("caca2")
                    continue

                #check if the ray and the side can intersect
                #if cx < dx:
                #    #biggest xside coordinate is smaller than ax, so no intersection
                #    if dx <= ax:
                #        continue
                #else:
                #    if cx <= ax:
                #        continue

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
                            #print(px,py)

                #print(px, side, bx, by)
            else:
                badRay = False


        if count % 2 == 1:
            res = "jackpot"
        else:
            res = "too bad"
        print("Case #{0}: {1}".format(case, res))



        if case < case_count:
            input()
