
class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node:
                node[char]= {}
            node = node[char]
        node["*"] = 'end'
        # print(self.root)

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char in node:
                node = node[char]
            else:
                return False
        return "*" in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char in node:
                node = node[char]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)