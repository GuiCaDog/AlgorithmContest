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
        n, k, r, d = map(int, sys.stdin.readline().split())

        keep = [0]*(n+1)
        keepUF = UF(n+1)
        rmve = [0]*(n+1)
        rmveUF = UF*(n+1)
        
        okConflict = "ok"
        if k != 0 and r!=0:
            firstKeep = int(input())
            for i in range(1, k):
                pckge = int(input())
                keepUF.union(firstKeep, pckge)
                keep[pckge] = 1
            firstRemove = int(input())
            if keep[firstRemove] == 1:
                okConflict = "conflict"
            else:
                for i in range(1, r):
                    pckge = int(input())
                    rmveUF.union(firstRemove, pckge)

                    #we detect keep and remove have 1 in common, stop
                    if keep[pckge] == 1:
                        okConflict = "conflict"
                        break
                    rmve[pckge] = 1
                if okConflict == "ok":

                    for i in range(0, d):
                        u,de = map(int, sys.stdin.readline().split())
                        keepUF.union(u, de)
                        rmveUF.union(u, de)
                        if keep[u] == 1:
                            if rmve[de] == 1:
                                okConflict = "conflict"
                                break
                            keep[de] = 1

                        elif rmve[de] == 1:
                            rmve[u] = 1

                if okConflict == "ok":
                    for i in range(1, n+1):
                        keepRep = keepUF.find(firstKeep)
                        if keepUF.find(i) == keepRep:
                            keep[i] = 1

                    for i in range(1, n+1):
                        rmveRep = rmveUF.find(firstRemove)
                        if keepUF.find(i) == keepRep and keep[i] == 1:
                            okConflict = "conflict"
                            break
                

        print("Case #{0}: {1}".format(case, okConflict))

        if case < case_count:
            input()
