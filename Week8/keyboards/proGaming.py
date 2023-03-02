import sys
import math



def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        
        s1, c1, s2, c2, n =map(int, sys.stdin.readline().split())
        
        aLowBound = max(math.ceil((n - s1) / c1), 0)

        a = max(aLowBound, 0)
        if (s1 - s2) % gcd(c1, c2) != 0:
            res = "impossible"
        else:
            for a in range(aLowBound, aLowBound + 10000000):
                b = ((s1-s2) + c1*a) 
                if b>=0 and b % c2 == 0:
                    break
            #else:
            #    res = "impossible" 
            #
            #if res != "impossible":
            #    res = s1 + c1*a
            res = s1 + c1*a
        print("Case #{0}: {1}".format(case, res))
