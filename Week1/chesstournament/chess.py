import sys

#If the teams are exactly equals, we return t1
def compareTeams(t1, t2):

    i = 0
    while i < len(t1):
        if t1[i] > t2[i]:
            return 1 
        elif t1[i] < t2[i]:
            return -1 
        i+=1

    return 0 

def mergeTeams(m1, m2):
    i = 0
    j = 0
    m = []
    while i < len(m1) and j < len(m2):
        if compareTeams(m1[i], m2[j]) > 0:
            m.append(m1[i])
            i += 1
        elif compareTeams(m1[i], m2[j]) < 0:
            m.append(m2[j])
            j += 1
        else:
            m.append(m1[i])
            m.append(m2[j])
            i+=1
            j+=1

    while i < len(m1):
        m.append(m1[i])
        i+=1

    while j < len(m2):
        m.append(m2[j])
        j+=1

    return m
 



def mergeSortRows(teams, ini, fi):
    if ini == fi:
        l = []
        l.append(teams[ini])
        return l

    m = int((fi + ini) / 2)
    m1 = mergeSortRows(teams, ini, m)
    m2 = mergeSortRows(teams, m+1, fi)
    return mergeTeams(m1, m2)

if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):

        #getting rid of the blank line
        if case > 1:
            input()

        nTeams = int(input())
        teams = []

        for t in range(0, nTeams):
            #Creating TeamsMatri
            team = sys.stdin.readline().split()
            team = [int(i) for i in team]
            teams.append(sorted(team, reverse=True))
        
        #Sorting the teams
        teams = mergeSortRows(teams,0,len(teams)-1)
       
        print("Case #{0}:{1}".format(case, ""))
        for team in teams:
            team = [str(i) for i in team]
            print(" ".join(team))

    

