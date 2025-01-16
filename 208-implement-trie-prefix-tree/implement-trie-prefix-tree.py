class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
             #curr.count+=1 
        curr.is_end = True

    
    def search(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                return False
            else:
                curr = curr.children[ch]
             #curr.count+=1 
        return curr.is_end == True

        # check the word is "$" : searchword
        # search prefix "$" is not end
        pass 
    
    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for ch in prefix:
            if ch not in curr.children:
                return False
            else:
                curr = curr.children[ch]
             #curr.count+=1 
        return True # ends here as well as startswith
    



    
# class Trie:

#     def __init__(self):
#         self.root = {}

#     def insert(self, word: str) -> None:
#         node = self.root

#         for char in word:
#             if char not in node:
#                 node[char]= {}
#             node = node[char]
#         node["*"] = 'end'


#     def search(self, word: str) -> bool:
#         node = self.root
#         for char in word:
#             if char in node:
#                 node = node[char]
#             else:
#                 return False
#         return "*" in node

#     def startsWith(self, prefix: str) -> bool:
#         node = self.root
#         for char in prefix:
#             if char in node:
#                 node = node[char]
#             else:
#                 return False
#         return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)