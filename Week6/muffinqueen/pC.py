from collections import defaultdict

t = int(input())
n,m = 0,0
foundAnswer = False

def dfs(baker, happy, nhappy):
    #print(baker, nhappy, n, m)
    #print("b: ", baker, m, nhappy)
    #print(happy)

    # Everybody is happy
    if nhappy >= n:
        global foundAnswer
        foundAnswer = True
        return
    # This means we have come to an end
    if baker > m:
        return

    branched = False
    for i in range(len(prefs[baker])):
        print("aaaa", i)
        judge = prefs[baker][i]
        if not happy[judge]:
            newHappy = happy.copy()
            newHappyCounter = nhappy
            newHappyCounter += 1
            newHappy[judge] = True
            i += 1
            while i < len(prefs[baker]):
                judge = prefs[baker][i]
                if not happy[judge]:
                    #print(judge)
                    newHappyCounter +=1
                    newHappy[judge] = True
                i+=1
            branched = True
            dfs(baker+1, newHappy, newHappyCounter)

    branched2 = False
    for judge in prefs[-baker]:
        if not happy[judge]:
            #print(judge)
            nhappy += 1
            happy[judge] = True
            branched2 = True

    if branched2:
        dfs(baker+1, happy, nhappy)
    if not branched and not branched2:
        dfs(baker+1, happy, nhappy)
    

    


for i in range(t):
    prefs = defaultdict(list)
    print("Case #" + str(i+1) + ": ", end='')
    m, n  = map(int, input().rstrip().split())
    foundAnswer = False
    #print(m, n)
    for j in range(n):
        l = list(map(int, input().rstrip().split()))
        for elem in l:
            if elem != 0:
                prefs[elem].append(j)

    #print(dict(prefs))

    happy = [False]*n
    dfs(1, happy, 0)

    if foundAnswer:
        print("yes")
    else:
        print("no")
