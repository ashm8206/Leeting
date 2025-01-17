class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end = False
        # self.word = []

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
        # node.word.append(word)

    def search(self, word: str) -> bool:
        # res = []
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

        if node.is_end:
            # res.append(node.word
            return True
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)