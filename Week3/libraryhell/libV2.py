import sys
from collections import deque

if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n, k, r, d = map(int, sys.stdin.readline().split())

        keep = {}
        roots = []
        rmve = [0]*(n+1)
       
        okConflict = "ok"
        if k != 0 and r!=0:
            roots = sys.stdin.readline().split()
            roots = [int(i) for i in roots]

            removals = sys.stdin.readline().split()
            removals = [int(i) for i in removals]

            for pckge in removals:
                rmve[pckge] = 1

            for i in range(0, d):
                u,de = map(int, sys.stdin.readline().split())
                adys = keep.get(u, [])
                adys.append(de)
                keep[u] = adys

            visited = [0]*(n+1)
            exploring = deque() 

            for root in roots:
                if rmve[root] == 1:
                    okConflict = "conflict"
                    break
                if visited[root] != 1:
                    exploring.append(root)

                while len(exploring) != 0:
                    exp = exploring.pop()
                    visited[exp] = 1

                    for dep in keep.get(exp,[]):
                        if rmve[dep] == 1:
                            okConflict = "conflict"
                            break
                        if visited[dep] != 1:
                            exploring.append(dep)
                    if okConflict == "conflict":
                        break
                if okConflict == "conflict":
                    break

        else: #k or r is 0 (or both)
            sys.stdin.readline()
            sys.stdin.readline()
            for i in range(0, d):
                sys.stdin.readline()

        print("Case #{0}: {1}".format(case, okConflict))

        if case < case_count:
            input()
