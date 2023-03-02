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
        n, k = map(int, sys.stdin.readline().split())
        
        if n != 0:
            m = [0] * n
            a = [0] * n
            for i in range(0, n):
                mi, ai = map(int, sys.stdin.readline().split())
                m[i] = mi
                a[i] = ai 

            w = [0] * n
            z = [0] * n
            M = 1
            for i in range(0, n):
                M *= m[i]

            for i in range(0, n):
                z[i] = M // m[i]

            zInv=[0]*n
            res = ""
            for i in range(0, n):
                zInv[i] = muInv(z[i], m[i])
                #print(zInv[i], pow(z[i], -1, m[i])) 
                if zInv[i] == 0:
                    print("Case #{0}: {1}".format(case, "impossible"))
                    break
            
            else:
                w = [0]*n

                for i in range(0, n):
                    w[i] = z[i]*zInv[i]
                X = 0 
                for i in range(0, n):
                    X+= a[i]*w[i]     

                if X > k:
                    a=math.ceil(-(k-X)/M)
                    X-=a*M
                else:
                    a=(k-X)//M
                    X+=a*M
                #for i in range(0, 10):
                #    print(X-M*i)
                if X < 0:
                    print("Case #{0}: {1}".format(case, "impossible"))
                else:
                    print("Case #{0}: {1}".format(case, X))
        else:
            print("Case #{0}: {1}".format(case, 0))

        if case < case_count:
            input()
