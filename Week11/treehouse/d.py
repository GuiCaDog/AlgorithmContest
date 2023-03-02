import sys
import math
from collections import deque


INF = 10000000000
def buildTree(array): #with stack
    ini = 0
    end = len(array) - 1
    h = math.ceil(math.log2(len(array)))
    tree = [INF]*pow(2, h+1)
    stack = deque()
    stack.append((1, ini, end))

    while len(stack) > 0:
        node, left, right = stack.pop()

        if left == INF & right == INF:
            tree[node] = min(tree[node*2],tree[node*2+1])

        elif left == right:
            tree[node] = array[left]
        
        else:
            stack.append((node, INF, INF))
            mid = (left + right) // 2
            stack.append((node*2, left, mid))
            stack.append((node*2+1, mid+1, right))

    return tree

def propagate(node, l, r):
    if lazy[node] != 0:
        tree[node] = min(lazy[node], tree[node])

        if l != r: #not a leaf
            lazy[2*node] = min(lazy[node], lazy[2*node])
            lazy[2*node+1] = min(lazy[node], lazy[2*node])

        lazy[node] = 0

def rangeAdd(tree, lazy,size, l, r, v):
    stack = deque()
    ini = 0
    end = size-1
    stack.append((1, ini, end))

    while len(stack) > 0:

        node, left, right = stack.pop()
        
        #"recursion" ended on children
        if left == INF and right == INF:
            tree[node] = min(tree[node*2], tree[node*2+1])

        else:
            propagate(node, left, right)
            
            if left > right or left > r or right < l:#no overlap
                #nothing to do to this node
                continue
            
            elif l <= left and right <= r:#total overlap
                #update node
                tree[node] = min(v, tree[node])
                
                #add lazy value to children
                if left != right:
                    lazy[node*2] = min(v, lazy[node*2])
                    lazy[node*2+1] = min(v, lazy[node*2+1])
            else:#partial overlap

                stack.append((node, INF, INF))
                m = (left + right) // 2
                stack.append((node*2, left, m))
                stack.append((node*2+1, m+1, right))

def rangePeek(tree, size, l, r):

    stack = deque()
    ini = 0
    end = size-1
    stack.append((1, ini, end))

    res = [] 
    while len(stack) > 0:

        node, left, right = stack.pop()
        
        #propagate(node, left, right)
            
        if left > right or left > r or right < l:#no overlap
            #nothing to do to this node
            continue
        
        elif l <= left and right <= r:#total overlap
            res.append(tree[node])
            
        else:#partial overlap

            m = (left + right) // 2
            stack.append((node*2, left, m))
            stack.append((node*2+1, m+1, right))

    return min(res)

def etr(depth, tree, root):
    res = [root]
    depths = [depth]
    for child in tree.get(root,[]):
        etri, depthi = etr(depth+1, tree, child)
        for node in etri:
            res.append(node)
        res.append(root)
        for d in depthi:
            depths.append(d)
        depths.append(depth)
    return res, depths

def stackEtr(depth, tree, root):
    res = []
    depths = []
    stack = deque()
    stack.append((root, depth, 1))
    while len(stack) > 0:
        curRoot, curDepth, flag = stack.pop()
        res.append(curRoot)
        depths.append(curDepth)
        if flag == 1:
            for child in tree.get(curRoot,[]):
                stack.append((curRoot,curDepth, -1))
                stack.append((child, curDepth+1,1))
    return res, depths

def lca(u,v,firstOcurrences,segTree, etr, depths):
    if firstOcurrences[u] < firstOcurrences[v]:
        x = firstOcurrences[u]
        y = firstOcurrences[v]
    else:
        x = firstOcurrences[v]
        y = firstOcurrences[u]

    minAncesDepth = rangePeek(segTree, len(depths), x, y)
    
    #print(minAncsDepth)
    #print(x, y)
    #for i in range(x, y):
    #    if depths[i] == minAncsDepth:
    #        return etr[i]
    return minAncesDepth


if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n = int(input()) 
        treeHouse = {-1: [-1]*(n+1)} #-1 refers to "parents" array
        treeHouse[-1][1] = 1
        for i in range(1, n+1):
            children = sys.stdin.readline().split()
            for j in range(1, int(children[0])+1):
                child = int(children[j])
                treeHouse[i] = treeHouse.get(i, [])
                treeHouse[i].append(child)
                treeHouse[-1][child] = i

        toVisit = sys.stdin.readline().split()
        toVisit = [int(toVisit[i]) for i in range(1, len(toVisit))]

        

        #h = math.ceil(math.log2(n))
        #tree = [0]*pow(2, h+1)
        #lazy = [0]*pow(2, h+1)
        #
        #for q in queries:
        #    highestBelow=rangePeek(tree, lazy, n, q[2],q[2]+q[0]-1)
        #    rangeAdd(tree, lazy, n, q[2],q[2]+q[0]-1,highestBelow + q[1])
        #    print(rangePeek(tree, lazy, n, 0, n-1), end = " ")
        #    #print(tree)
        #print()
        #print(treeHouse)
        #print(toVisit)
        res, depths = stackEtr(0,treeHouse,1)
        #print(res,depths)
        #print(stackEtr(0,treeHouse, 1))
        firstVisited = [-1]*(n+1)
        for i in range(len(res)):
            if firstVisited[res[i]] == -1:
                firstVisited[res[i]] = i

        segTree = buildTree(depths)
        
        vDepth = depths[firstVisited[toVisit[0]]]
        branches = vDepth
        for i in range(len(toVisit)-1):
            u = toVisit[i]
            uDepth = depths[firstVisited[u]]
            v = toVisit[i+1]
            vDepth = depths[firstVisited[v]]
            lcaDepth = lca(u, v, firstVisited, segTree, res, depths)
            #print(uDepth, vDepth, lcaDepth)
            branches += (abs(uDepth-lcaDepth) + abs(vDepth-lcaDepth))

        print("Case #{0}: {1}".format(case,branches))


        if case < case_count:
            input()
