import sys
import math

if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        d, p, u, v = map(int, sys.stdin.readline().split())
       
        #minDistance if no gap
        noGapD = d/(p-1)
        #posts before gap
        nPostsBeGap = math.floor((u / noGapD)) + 1

        #How many are inside the gap?
        nPostsInGap = math.floor((v / noGapD)) + 1 - nPostsBeGap
        
        if math.floor((v / noGapD))*noGapD == v and v != u: #A post in the end of the gap is not inside
            nPostsInGap -= 1

        #How many are after the gap?
        nPostsAfGap = math.floor((d / noGapD)) + 1 - nPostsBeGap - nPostsInGap

        #print(nPostsBeGap, nPostsInGap, nPostsAfGap)
        #Now we need to distribute the posts that are inside the gap
        maxDistance = noGapD
        if nPostsInGap > 0:  
            #posts that go to the left
            leftPosts = 0

            #posts that go to the right
            rightPosts = nPostsInGap

            maxDistance = 0
            
            #we calculate the min distance for all posibilities
            #and get the max
            for i in range(0, int(nPostsInGap) + 1):
                
                if leftPosts+i > 0:
                    leftMinD = u / ((nPostsBeGap-1) + leftPosts+i)
                else:
                    leftMinD = noGapD

                if rightPosts - i > 0:
                    rightMinD = (d-v) / ((nPostsAfGap-1) + rightPosts-i)
                else:
                    rightMinD = noGapD 

                minPossible = min(leftMinD, rightMinD)

                if maxDistance < minPossible:
                    maxDistance = minPossible


        print("Case #{0}: {1:.10f} ".format(case, maxDistance))

