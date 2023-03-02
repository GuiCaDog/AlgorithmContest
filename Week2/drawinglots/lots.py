import sys

def aproximate(prices, increments, cost):
    prob = 0
    for incr in increments:
        
        for i in range(0, 10):
            aproximation = 0
            
            exp = 1
            for p in prices:
                aproximation += p*(pow((prob+incr*i), exp))
                exp += 1

            if aproximation > cost:
                prob += incr*(i-1)
                break
            if aproximation == cost:
                return prob + incr*i

        else:
            prob += incr*9 

    return prob

        


if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n, b = map(int, sys.stdin.readline().split())

        prizes = sys.stdin.readline().split()
        prizes = [int(i) for i in prizes]
       
        prob = 0
        aproximation = 0
        incr = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001, 0.000000001, 0.0000000001, 0.00000000001, 0.000000000001]
        prob = aproximate(prizes, incr, b)
        print("Case #{0}: {1:.10f}".format(case, prob))

        if case < case_count:
            input()
