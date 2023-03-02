import sys
import math




def eGcd(a, b):
    if b == 0:
        return [a, 1, 0]
    else:
        g, xP, yP = eGcd(b, a % b)
        #g = xP*b + yP*(a % b)
        x = yP
        y = xP - (a // b) * yP
        #g = x*a + y*b
        #g = yP*a + xP*b - yP*(a//b)*b
        #g = yP(a - (a//b)*b) + xP*b
        #g = xP*b + yP(a - (a//b)*b) = xP*b + yP(a % b)
        return [g, x, y]

def muInv(z, m):
    g, x, y = eGcd(z, m)
    if g == 1:#1 = x*z + y*m -> 1 mod m = (xz mod m + ym mod m) mod m
        #1 = xz mod m -> xz --- 1 (mod m)
        return x % m 
    else: #has no multiplicative inverse
        return 0 


if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n, y = map(int, sys.stdin.readline().split())
        
        x = muInv(y, pow(10,n))
        if x == 0:
            print(":S")
        print("Case #{0}: {1}".format(case, x))

