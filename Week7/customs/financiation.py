import sys



if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n = int(input()) 
        
        myTerritory = [0]*(n+1)
        cities = {} 
        for i in range(1, n+1):
            city = [int(r) for r in sys.stdin.readline().split()][1:]
            cities[i] = cities.get(i, [])
            for c in city:
                if c not in cities[i]:
                    cities[i].append(c)

            for c in city:
                cities[c] = cities.get(c, [])
                if i not in cities[c]:
                    cities[c].append(i)
                       
        new_dic={}
        k = list(cities.items())
        k.sort(key=lambda x:len(x[1]),reverse=True)
        
        for i in k :
            new_dic.update({i[0]:i[1]})
        
        cities = new_dic
        myTerritory[1] = 1
        
        cities.pop(1)
        popped = 1

        while popped > 0: 
            maxOutMinusIn = -1 
            maxC = -1
            popped = 0
            for c in list(cities.keys()):
                if maxOutMinusIn > len(cities[c]):
                    break

                #cities that c can give:
                citiesOut = 0
                citiesIn  = 0
                for city in cities[c]:
                    if myTerritory[city] == 0:
                        citiesOut += 1
                    else:
                        citiesIn += 1

                if citiesOut - citiesIn > 0:
                    if citiesOut - citiesIn > maxOutMinusIn:
                        maxOutMinusIn = citiesOut - citiesIn
                        maxC = c

            if maxC != -1:
                myTerritory[maxC] = 1
                cities.pop(maxC)
                popped = 1
                    

        print("Case #{0}:".format(case))

        res = ""
        for i in range(1, n+1):
            if myTerritory[i] == 1:
                res+= str(i) + " "
        res = res[:-1]
        print(res)
        if case < case_count:
            input()
