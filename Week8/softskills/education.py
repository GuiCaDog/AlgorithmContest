import sys
import math
def primeBinom(n, m, p):
    if m > n:
        return 0
    if m > n-m:
        num = 1
        for i in range(m+1, n+1):
            num=(num*i) % p 
    
        den = 1
        for i in range(1, n-m+1):
            den=(den*i) % p

    else:
        num = 1
        for i in range((n-m)+1, n+1):
            num=(num*i) % p 
    
        den = 1
        for i in range(1, m+1):
            den=(den*i) % p

    res = num * pow(den, p-2, p) % p 
    return res

def lucaBinom(n, m, p):
    nDigits = pBaseDigits(n,p)
    mDigits = pBaseDigits(m,p)
    binom = 1
    for i in range(0, len(nDigits)):
        ni = nDigits[i] 
        if i < len(mDigits):
            mi = mDigits[i]
            binom = (binom*primeBinom(ni, mi, p)) % p
        else:
            return binom 

    return binom

def pBaseDigits(n, p):
    digits = []


    r = n % p
    q = n // p
    digits.append(r)
    while q >= p:
        r = q % p
        q = q // p
        digits.append(r)

    digits.append(q)
    
    return digits

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

def chineseRemainder(m, a):
    n = len(m)
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
        if zInv[i] == 0:
            return -1
            break
    
    else:
        w = [0]*n
    
        for i in range(0, n):
            w[i] = z[i]*zInv[i]
        X = 0
        for i in range(0, n):
            X+= a[i]*w[i]
    
        return X


if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):

        n, m = map(int, sys.stdin.readline().split())
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        remainders = []
        for p in primes:
            remainders.append(lucaBinom(n,m,p))
        
        res = chineseRemainder(primes, remainders) % 223092870

        print("Case #{0}: {1}".format(case,res))

#        if case < case_count:
#            input()
