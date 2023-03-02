import sys
import math
from collections import deque


INF = 10000000000
#def buildTree(array): #with stack
#    ini = 0
#    end = len(array) - 1
#    h = math.ceil(math.log2(len(array)))
#    tree = [0]*pow(2, h+1)
#    stack = deque()
#    stack.append((1, ini, end))
#
#    while len(stack) > 0:
#        node, left, right = stack.pop()
#
#        if left == INF & right == INF:
#            tree[node] = tree[node*2]+tree[node*2+1]
#
#        elif left == right:
#            tree[node] = array[left]
#        
#        else:
#            stack.append((node, INF, INF))
#            mid = (left + right) // 2
#
#            stack.append((node*2, left, mid))
#            stack.append((node*2+1, mid+1, right))

def propagate(node, l, r):
    if lazy[node] != 0:
        tree[node] = max(lazy[node], tree[node])

        if l != r: #not a leaf
            lazy[2*node] = max(lazy[node], lazy[2*node])
            lazy[2*node+1] = max(lazy[node], lazy[2*node])

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
            tree[node] = max(tree[node*2], tree[node*2+1])

        else:
            propagate(node, left, right)
            
            if left > right or left > r or right < l:#no overlap
                #nothing to do to this node
                continue
            
            elif l <= left and right <= r:#total overlap
                #update node
                tree[node] = max(v, tree[node])
                
                #add lazy value to children
                if left != right:
                    lazy[node*2] = max(v, lazy[node*2])
                    lazy[node*2+1] = max(v, lazy[node*2+1])
            else:#partial overlap

                stack.append((node, INF, INF))
                m = (left + right) // 2
                stack.append((node*2, left, m))
                stack.append((node*2+1, m+1, right))

def rangePeek(tree, lazy, size, l, r):

    stack = deque()
    ini = 0
    end = size-1
    stack.append((1, ini, end))

    res = [] 
    while len(stack) > 0:

        node, left, right = stack.pop()
        
        propagate(node, left, right)
            
        if left > right or left > r or right < l:#no overlap
            #nothing to do to this node
            continue
        
        elif l <= left and right <= r:#total overlap
            res.append(tree[node])
            
        else:#partial overlap

            m = (left + right) // 2
            stack.append((node*2, left, m))
            stack.append((node*2+1, m+1, right))

    return max(res)

if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n, k = map(int, sys.stdin.readline().split())
        
        queries = []
        for i in range(0, k):
            querie = sys.stdin.readline().split()
            queries.append([int(querie[0]), int(querie[1]), int(querie[2])])
        

        h = math.ceil(math.log2(n))
        tree = [0]*pow(2, h+1)
        lazy = [0]*pow(2, h+1)
        
        print("Case #{0}: ".format(case), end="")
        for q in queries:
            highestBelow=rangePeek(tree, lazy, n, q[2],q[2]+q[0]-1)
            rangeAdd(tree, lazy, n, q[2],q[2]+q[0]-1,highestBelow + q[1])
            print(rangePeek(tree, lazy, n, 0, n-1), end = " ")
            #print(tree)
        print()



        if case < case_count:
            input()
