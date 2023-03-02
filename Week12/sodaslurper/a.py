import sys



if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        e,f,c = map(int, sys.stdin.readline().split())
        
        available = e + f
        consumed = 0
        while available >= c:
            consumed+= available // c
            available = available // c + available % c

        print("Case #{0}: {1}".format(case, consumed))

        #if case < case_count:
        #    input()
