import sys



if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n, m, l = map(int, sys.stdin.readline().split())
        
        pred = {}
        graf = {}

        for i in range(1, n+1):
            pred[i] = {}
        
        #how to know if a predecessor has also you as predecessor?
        #you go to him and check if you are a predecessor of him
        #if that's the case, you skip counting that predecessor of yours
        #but, now you will be his predecessor

        for i in range(0, m):
            direct = sys.stdin.readline().split()
            u = int(direct[0])
            v = int(direct[1])
            pred[v][u] = 1

            #we also create the proper city graf
            graf[u] = graf.get(u, [])
            graf[u].append(v)
        
        biEdges = []
        for i in range(0, l):
            bidirect = sys.stdin.readline().split()
            u = int(bidirect[0])
            v = int(bidirect[1])
            pred[v][u] = 1
            pred[u][v] = 1
            biEdges.append([u, v, v, u])

            #we also create the proper city graf
            graf[v] = graf.get(v, [])
            graf[v].append(u)
            graf[u] = graf.get(u, [])
            graf[u].append(v)

        intersects = list(pred.keys())
        #vertex sorted by increasing number of predecessors
        intersects = sorted(intersects, key=lambda x: len(pred[x]))

        topologicalOrder = []
        edgesChanged = [] 
        deletedOne = 1
        #print(intersects)
        while len(topologicalOrder) != n and deletedOne == 1:
            #print(pred)
            deletedOne = 0
            for v in intersects:
                #can we make v to have no predecessors?
                nPredV = len(pred[v])
                #count how many of v edges, are bidirectional
                nBi = 0
                for pre in pred[v]:
                    #pre is a predecessor of v,
                    if pred.get(pre, {}).get(v,0) == 1:  #but also v is a predecessor of pre
                        nBi +=1

                if nBi == nPredV: #actually, we can make v to have no predecessors
                    #let's do it
                    for pre in list(pred[v]):
                        pred[v].pop(pre, None)
                        #we need to remove the edge that was pointing to v
                        graf[pre].remove(v)

                        edgesChanged.append([v, pre])
                #print(graf[v])
                if len(pred[v]) == 0: #this v has 0 predecessors
                    #for each of his sons, we delete him as a predecessor
                    for son in list(graf.get(v,[])):
                        #print(son)
                        #print(pred[son], v)
                        pred[son].pop(v, None)
                        graf[v].remove(son)
                    topologicalOrder.append(v)
                    #we remove it from graf and from pred
                    pred.pop(v, None)
                    graf.pop(v, None)
                    intersects.remove(v)
                    deletedOne = 1
        
        yesNo = "yes"
        if len(topologicalOrder) != n:
            yesNo = "no"



        print("Case #{0}: {1}".format(case, yesNo))
        if yesNo == "yes":
            for bi in biEdges:
                for edge in edgesChanged:
                    if bi[0]==edge[0] and bi[1]==edge[1] or bi[2]==edge[0] and bi[3]==edge[1]:
                        print(str(edge[0]) + " " + str(edge[1]))

        if case < case_count:
            input()
