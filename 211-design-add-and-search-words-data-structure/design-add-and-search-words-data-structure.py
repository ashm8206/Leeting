class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        return self.searchWord(word, self.root)
    
    def searchWord(self, word, root):
        node = root
        for i, c in enumerate(word):
            if c not in node.children: 
                if c == ".":
                    for c in node.children:
                        if self.searchWord(word[i+1:], node.children[c]):
                            return True
                return False # any other character, or match not found
            else:
                node = node.children[c]
        return node.is_end==True
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)