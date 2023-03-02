import sys




def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n = int(input()) 
        
        armies = sys.stdin.readline().split()
        armies = [int(i) for i in armies]
        
        lastGcd = 0
        for a in armies:
            lastGcd = gcd(a, lastGcd)

        print("Case #{0}:".format(case))
        print(lastGcd)
        if case < case_count:
            input()
