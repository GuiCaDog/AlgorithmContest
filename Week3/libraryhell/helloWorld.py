import sys

if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n, k, r, d = map(int, sys.stdin.readline().split())

        keep = [0]*(n+1)
        rmve = [0]*(n+1)
        
        okConflict = "ok"
        for i in range(0, k):
            pckge = int(input())
            keep[pckge] = 1
        for i in range(0, r):
            pckge = int(input())
            if keep[pckge] == 1:
                okConflict = "conflict"
                break
            rmve[pckge] = 1
        if okConflict == "ok":

            dependencies = []
            for i in range(0, d):
                u,de = map(int, sys.stdin.readline().split())
                dependencies.append([u,de])
                if keep[u] == 1:
                    if rmve[de] == 1:
                        okConflict = "conflict"
                        break
                    keep[de] = 1

                elif rmve[de] == 1:
                    rmve[u] = 1

        if okConflict == "ok":
            for dep in dependencies:
                if keep[dep[0]] == 1 and rmve[dep[1]] == 1:
                    okConflict = "conflict"
                    break
                

        print("Case #{0}: {1}".format(case, okConflict))

        if case < case_count:
            input()
