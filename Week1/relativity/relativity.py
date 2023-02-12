import sys

if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    c = 299792458
    for case in range(1, case_count + 1):
        m = int(input()) 
        print("Case #{0}: {1}".format(case, m*c*c))
