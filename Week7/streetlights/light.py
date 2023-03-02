import sys



if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        le, n, r = map(int, sys.stdin.readline().split())
        
        lights = sorted([int(p) for p in sys.stdin.readline().split()])        
        lastBorder = 0
        post = 0
        countPosts = 0
        while lastBorder < le and post < len(lights):
            #The distance between the last border
            #And the next post, has to be smaller 
            #or equal than r but maximum

            #we stop when the next post is no longer valid
            while post < len(lights)-1 and lights[post+1] - lastBorder <= r:
                post+=1
           
            #the first post that we considered, is already not useful
            if lights[post] - r > lastBorder:
                break

            lastBorder = lights[post] + r
            countPosts += 1
            post += 1        

        res = countPosts
        if lastBorder < le:
            res = "impossible"
        
        print("Case #{0}: {1}".format(case, res))

        if case < case_count:
            input()
