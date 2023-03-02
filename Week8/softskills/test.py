import sys
import math



if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):

        n, k = map(int, sys.stdin.readline().split())

        if(k > n - k):
            k = n - k
        # initialize result
        num = 1
        den = 1
        # Calculate value of
        # [n * (n-1) *---* (n-k + 1)] / [k * (k-1) *----* 1]
        for i in range(k):
            num = num*((n-i)%223092870)
            den = den*((i+1)%223092870)
            print(num, den)
                
        print("Case #{0}: {1}".format(case, num))
        print(den)
        print(num/den)



#        if case < case_count:
#            input()
