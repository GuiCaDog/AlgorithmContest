import sys
import math

if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        d, p, u, v = map(int, sys.stdin.readline().split())

        minD = d

        #space around the gap
        sNoGap = u + (d-v)


        if sNoGap == 0:#gap is all the space
            if p > 2:#We've got to put more than 2 posts, some will be at the same point
                minD = 0
        else:
            sBeGap = u / sNoGap # proportional [0,1] space at the left 
            sAfGap = (d-v) / sNoGap #proportional [0,1] space at the right 
    
            pBeGap = sBeGap * (p-2) #posts that will be at the left (except the one at 0)
            pAfGap = sAfGap * (p-2) #posts that will be at the right (except the one at d)

            #fracBe, whole = math.modf(pBeGap) 
            #if fracBe == 0.5: #case rounding won't work well

            #We have to see which part would become less stretched 
            #To decide where to put the one that represents the decimal part

            if pBeGap != 0 and pAfGap != 0:
                if u / (math.ceil(pBeGap)) > (d-v) / ( math.ceil(pAfGap)):
                    pBeGap = math.ceil(pBeGap) 
                    pAfGap = math.floor(pAfGap) 
                else:
                    pBeGap = math.floor(pBeGap)
                    pAfGap = math.ceil(pAfGap)

            elif pBeGap == 0:
                pAfGap = math.ceil(pAfGap)

            else:
                pBeGap = math.ceil(pBeGap)
            
            #position of posts closest to the gap
            closestFromLeft= minD*pBeGap
            closestFromRight = d-minD*pAfGap
           
            #distances from closests to u and v
            dToU = abs(u - closestFromLeft)
            dToV = abs(closestFromRight - v)

            #distance between closests
            dClosests = closestFromRight - closestFromLeft

            #difference between dClosests and minD
            difDisClosMinD = abs(dClosests - minD)
            
            ini = 0
            fi = d
            while (pBeGap == 0 or dToU > 0.0001) and (pAfGap == 0 or dToV > 0.0001) and difDisClosMinD > 0.0001 or (closestFromLeft > u or closestFromRight < v or dClosests < minD):

                #With minD, posts reach past the gap, or are too close between them
                if closestFromLeft > u or closestFromRight < v or dClosests < minD:
                    fi = minD-0.0001 
    
                elif (pBeGap == 0 or closestFromLeft < u) and (pAfGap == 0 or closestFromRight > v)  and dClosests > minD:
                    ini = minD+0.0001 
    
                minD = (fi+ini) / 2

                #position of posts closest to the gap
                closestFromLeft= minD*pBeGap
                closestFromRight = d-minD*pAfGap
                
                #distances from closests to u and v
                dToU = abs(u - closestFromLeft)
                dToV = abs(closestFromRight - v)

                #distance between closests
                dClosests = closestFromRight - closestFromLeft

                #difference between dClosests and minD
                difDisClosMinD = abs(dClosests - minD)
    
        print("Case #{0}: {1:.10f} ".format(case, minD))

