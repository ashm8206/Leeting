# from collections import defaultdict

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        hashmap =  {}
        countPairs = 0
        for word in words:
            signature = self.getSignature(word)
            if (signature in hashmap.keys()):
                countPairs+= hashmap[signature] 
                # how many pairs can this new word make with existing?
                hashmap[signature]+=1 
            else:
                hashmap[signature] = 1
        return countPairs
        
    def getSignature(self, word) -> set:
        hashset = set()
        for char in word:
            hashset.add(char)
        return frozenset(hashset)
