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
        a, b, c = map(int, sys.stdin.readline().split())

        money = sys.stdin.readline().split()
        money = [0] + [int(i) for i in money]
                        
        families = UF(a)

        for i in range(0, b):
            d, e = map(int, sys.stdin.readline().split())
            families.union(d, e)

        marriages = {}

        for i in range(0, c):
            f, g = map(int, sys.stdin.readline().split())
            marriages[f] = 1
            marriages[g] = 1
            families.union(f,g)

        frees = []
        for p in range(1, len(money)):
            #We check that the person is free
            if families.find(p) != families.find(a) and marriages.get(p, None) == None:
                #We build the list of (money) persons who are free
                frees.append(money[p])
        if len(frees) > 0:
            richstAv = max(frees)
        else: 
            richstAv = "impossible"

        #returning argmax
        #f = lambda i: frees[i]
        #richstAv = max(range(len(frees)), key=f)

        
        print("Case #{0}: {1}".format(case, richstAv))
        if case < case_count:
            input()
