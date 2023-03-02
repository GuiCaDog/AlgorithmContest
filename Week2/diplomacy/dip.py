import sys

class UF:
    def __init__(self, n):
        self.parent = [-1]*(n+1)
        self.size = [0]*(n+1)
        self.enemies = [None]
        #self.representatives = {}

        for i in range(1, len(self.parent)):
            self.parent[i] = i
            self.size[i] = 1
            self.enemies.append({})
    
    def find(self, a):
        root = a
        while True:
            parent = self.parent[root]
            if parent == root:
                break
            root = parent

        current = a
        while current != root:
            next_elem = self.parent[current]
            self.parent[current] = root
            current = next_elem

        return root

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b: #already merged
            return a
        
        #Update the root of the smaller component
        a_size, b_size = self.size[a], self.size[b]
        if a_size < b_size: 
            a, b = b, a
        #a will be next representative of the class
        self.parent[b] = a

        #we update the enemies of the new representative
        for enemy in self.enemies[b]:
            self.enemies[a][enemy] = 1

        # Update size
        self.size[a] = a_size + b_size

    def makeEnemies(self, a, en):

        a = self.find(a)
        en = self.find(en)

        self.enemies[a][en] = 1
        self.enemies[en][a] = 1


if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n, m = map(int, sys.stdin.readline().split())

        friendships = UF(n)
        hatreds = []
        for i in range(0, m):
            line = sys.stdin.readline().split()
            r,x,y = map(str, line)
            x = int(x)
            y = int(y)

            if r == "F":
                friendships.union(x, y)

            else:
                hatreds.append([x,y])

        for hat in hatreds:
            friendships.makeEnemies(hat[0], hat[1])

#--------------------Enemies of my friends, my enemies------------------#
        #THIS IS DONE AUTOMATICALLY CAUSE WE JUST CONSIDER GROUPS#

    #-------------Enemies of my enemies, are my friends------------#

        representants = [0]*(n+1)
        for c in range(1, n+1):
            me = friendships.find(c)
            if representants[me] == 0:
                representants[me] = 1
                enemies = list(friendships.enemies[me].keys())
                for en in enemies:
                    newFriends = list(friendships.enemies[en].keys())
                    for newFriend in newFriends:
                        friendships.union(me, newFriend)
                me = friendships.find(me)
                representants[me] = 1

    #------------Counting how many friends has Lea-----------------#
        
        LeaFriends = friendships.find(1)
        nFriends = 1

        for c in range(2, n+1):
            if friendships.find(c) == LeaFriends:
                nFriends += 1
        
        yesNo = "no"
        if nFriends >= (n // 2) + 1:
            yesNo = "yes"


        print("Case #{0}: {1}".format(case, yesNo))
        #print(friendships.enemies)
        #print(hates)
        #print(friendships.parent)
        if case < case_count:
            input()
