import sys

class UF:
    def __init__(self, n):
        self.parent = [-1]*(n+1)
        self.size = [0]*(n+1)

        for i in range(1, len(self.parent)):
            self.parent[i] = i
            self.size[i] = 1
    
    def find(self, a):
        root = a
        while True:
            parent = self.parent[root]
            if parent == root:
                break
            root = parent

        current = a
        while current != root:
            next_elem = self.parent[current]
            self.parent[current] = root
            current = next_elem

        return root

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b: #already merged
            return a
        
        #Update the root of the smaller component
        a_size, b_size = self.size[a], self.size[b]
        if a_size < b_size: 
            a, b = b, a

        self.parent[b] = a
        # Update size
        self.size[a] = a_size + b_size


if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        
        #number of vertex
        n = int(input())

        conCom = UF(n) 
        edgesTot = []
        for i in range(1, n+1):

            edges = sys.stdin.readline().split()
            edges = [0] + [int(i) for i in edges]
            for j in range(i+1, n+1):
                edgesTot.append([i,j,edges[j]]) 

        edgesTot = sorted(edgesTot, key=lambda x: x[2])
        
        edPrint = {}
        for i in range(1, n+1):
            edPrint[i] = []
        #number of edges
        m = 0

        for edge in edgesTot:
            if m == n-1:#the graph is already connected
                break
            if conCom.find(edge[0]) != conCom.find(edge[1]):
                #now these vertex are in the same connected component
                conCom.union(edge[0], edge[1])
                #we have added an edge
                m+=1
                #we add the edge to the result
                edPrint[edge[0]].append([edge[0], edge[1]])

        print("Case #{0}:".format(case))

        for k in edPrint:
            edPrint[k] = sorted(edPrint[k], key=lambda x:x[1])
            for edge in edPrint[k]:
                print(str(edge[0]) + " " + str(edge[1]))
                        
        
        if case < case_count:
            input()
