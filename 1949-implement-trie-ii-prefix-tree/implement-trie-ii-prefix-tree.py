class TrieNode:

    def __init__(self):
        self.children = dict()
        self.count = 0
        self.is_end = False
        self.word_count = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] =  TrieNode()
            node = node.children[char]
            node.count+=1
        node.is_end = True
        node.word_count+=1
        
    def countWordsEqualTo(self, word: str) -> int:
        node = self.root

        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        
        if node.is_end:
            return node.word_count
        return 0 
        # It matched prefix, but word doesnt end here. so word not found
        

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root

        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]

        return node.count

    def erase(self, word: str) -> None:

        node = self.root

        for char in word:
            if char not in node.children:
                return
            node = node.children[char]
            node.count-=1

       
        node.word_count -=1

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)