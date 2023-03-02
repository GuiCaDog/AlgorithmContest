import sys

class Trie:
    def __init__(self, charToInt):
        super().__init__()
        self.charToInt = charToInt
        self.trie = {}
        self.lastId = 0

    def insert(self, word):
        
        trie = self.trie
        charToInt = self.charToInt

        source = 0
        target = None
        lastI = 0
        #traverse trie until no match found
        for i in range(len(word)):
            sourceSymbol = source*100 + charToInt[word[i]]
            target = trie.get(sourceSymbol, None)
            if target is not None:
                source = abs(target)
            else:
                lastI = i
                break
        else:
            trie[sourceSymbol]*=-1

        #insertNewChars
        for i in range(lastI, len(word)):
            sourceSymbol = source*100 + charToInt[word[i]]
            self.lastId += 1
            target = self.lastId
            source = target
            trie[sourceSymbol] = target
            if i == len(word) - 1:
                trie[sourceSymbol]*=-1




if __name__ == '__main__':
    case_count = int(sys.stdin.readline())
    for case in range(1, case_count + 1):
        n = int(input())
        
        intToChar = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        charToInt = {}
        for i in range(len(intToChar)):
            charToInt[intToChar[i]] = i
        
        trie = Trie(charToInt) 
        for i in range(n):
            contact = input()
            trie.insert(contact)
        
        sources = [0]*(trie.lastId+1)
        ends = []
        toRename = 0
        for source in trie.trie.keys():
            target = trie.trie[source] 
            if target < 0:
                ends.append(abs(target))
            realSource = source // 100
            sources[realSource] = 1

        for end in ends:
            if sources[end] == 1:
                toRename+=1
        


        print("Case #{0}: {1}".format(case, toRename))
        
        print(trie.trie)
        if case < case_count:
            input()
