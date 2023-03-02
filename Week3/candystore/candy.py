import sys

def buildMaxRelativeDistances(vther, me, tree, dtnces):

    for i in range(0, len(tree[me])):
        node = tree[me][i]
        # if I'm a son, and I'm visiting my father, I should note that this is my father.
        #I should not ask my father for his max distance
        if node == vther:
            # also, if I am a son, and I can just visit my father, I am a leaf
            if len(tree[me]) == 1:
                dtnces[me] = [[None, 0]]
        else:
            lgstThruNode = 0
            #son is going to build his max distances
            sonDists = buildMaxRelativeDistances(me, node, tree, dtnces)[node]
            maxes = []
            for d in sonDists:
                maxes.append(d[1])
            lgstThruNode = 1 + max(maxes)
            dtnces[me]= dtnces.get(me,[])
            dtnces[me].append([node, lgstThruNode])

            #dtnces[node] = dtnces.get(node,[])
            #dtnces[node].append(prof)
    

    return dtnces

def completeRelativeDistances(vther, me, tree, dtnces):
    for i in range(0, len(tree[me])):
        son = tree[me][i]
        if son != vther:
            maxes = []
            for d in dtnces[me]:
                if son != d[0]:
                    maxes.append(d[1])
            if len(maxes) == 0:
                dtnces[son].append([me, 1])
            else:
                dtnces[son] = dtnces.get(son,[])
                dtnces[son].append([me, 1 + max(maxes)])
            
            completeRelativeDistances(me, son, tree, dtnces)

if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        h = int(input())

        lindTown = {}
        farNbors = {}
        for hous in range(1, h+1):
            lindTown[hous] = []

        for e in range(0, h-1):
            u, v = map(int, sys.stdin.readline().split())
            lindTown[u].append(v)
            lindTown[v].append(u)
        
        farNbors = buildMaxRelativeDistances(1, 1, lindTown, farNbors)
        completeRelativeDistances(1, 1, lindTown, farNbors)

        mi = h
        minHouse = 1
        for house in farNbors:
            maxes = []
            for nB in farNbors[house]:
                maxes.append(nB[1])
            maxNnB = max(maxes)
            if maxNnB < mi:
                mi = maxNnB
                minHouse = house

        print("Case #{0}: {1}".format(case, minHouse))
        if case < case_count:
            input()
