import sys
import math



if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):

        n, k = map(int, sys.stdin.readline().split())

        prime_factors = [] 
        composite = [True] * 2 + [False] * n
        res = 1
        for p in range(n + 1):
            if composite[p]:
                continue
            
            q = p
            m = 1
            total_prime_power = 0
            prime_power = [0] * (n + 1)
            while True:
            
                prime_power[q] = prime_power[m] + 1
                r = q
            
                if q <= k:
                    total_prime_power -= prime_power[q]
            
                if q > n - k:
                    total_prime_power += prime_power[q]
            
                m += 1
                q += p
            
                if q > n:
                    break
            
                composite[q] = True
            
            prime_factors.append([p, total_prime_power])
            #for i in range(total_prime_power):
            #    res*=p
                
        print("Case #{0}: {1}".format(case, prime_factors))
        print(res)


#        if case < case_count:
#            input()
