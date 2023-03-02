import sys

if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        name = input() 
        print("Case #{0}: {1}".format(case,"Hello "+name+"!"))
