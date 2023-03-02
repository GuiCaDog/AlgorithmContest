import sys

class UF:
    def __init__(self, n):
        self.parent = [-1]*(n+1)
        self.size = [0]*(n+1)

        for i in range(1, len(self.parent)):
            self.parent[i] = i
            self.size[i] = 1
    
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

        self.parent[b] = a
        # Update size
        self.size[a] = a_size + b_size


if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n, m = map(int, sys.stdin.readline().split())

        friendships = UF(n)
        hates = {}

        for i in range(0, m):

            r,x,y = map(str, sys.stdin.readline().split())
            x = int(x)
            y = int(y)

            if r == "F":
                friendships.union(x, y)


            else:

                if hates.get(x, -1) == -1:
                    hates[x] = [y]
                else:
                    hates[x].append(y)

                if hates.get(y, -1) == -1:
                    hates[y] = [x]
                else:
                    hates[y].append(x)

 #--------------------Enemies of my friends, my enemies------------------#
    #-----(keeking always reciprocity in the relationships)------#
        friendsEnemies = {}
        #Creating common enemies
        for c in range(1, n+1):
            friend = friendships.find(c)
            if friendsEnemies.get(friend, -1) == -1:
                if hates.get(c, -1) == -1:
                    friendsEnemies[friend] = []
                else:
                    friendsEnemies[friend] = hates[c]
            else:
                if hates.get(c, -1) != -1:

                    #c is friend with find(c), so enemies of c, 
                    # are also enemies of everyone friend with find(c)
                    for en in hates[c]:
                        friendsEnemies[friend].append(en)

        #Eliminating possible duplicates
        for key in friendsEnemies:
            friendsEnemies[key] = list(set(friendsEnemies[key]))

        #Changing enemies of each country
        for c in range(1, n+1):
            friend  = friendships.find(c)
            hates[c] = friendsEnemies[friend]
        
        #Making enemy relation mutual
        for c in range(1, n+1):
            for en in hates[c]:
                if c not in hates[en]:
                    hates[en].append(c)

    #-------------Enemies of my enemies, are my friends------------#

        for c in range(1, n+1):
            for en in hates[c]:
                for enOfen in hates[en]:
                    friendships.union(c, enOfen)

        #So now, we need to join enemies, and not only with us, but with all our friends.

    #NOW I HAVE MORE FRIENDS, SO I NEED TO ADD THEIR ENEMIES AS MY ENEMIES?#
    #NO, BECAUSE I ALREADY HAD THE ENEMIES, THAT THESE NEW FRIENDS HAD#
    #FAAAAAAALSE, WE HAD 1 ENEMY IN COMMON, BUT PERHAPS THEY HAVE EVEN MORE ENEMIES T__________T#
    #ALSO NOBODY HAS INCREASED THE HATE THAT ALREADY HAD#

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
        #print(hates)
        #print(friendships.parent)
        if case < case_count:
            input()
