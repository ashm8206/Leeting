class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["$"] = True

    def search_node(self, word: str, node : dict) -> bool:
        # {'a': {'$': True}}
        for i, char in enumerate(word):
            
            if char == ".":
                for key in node.keys():
                    # print(node, word)
                    if key!='$' and self.search_node(word[i+1:],node[key]):
                        # print("am i here?")
                        return True
                return False
            elif char in node:
                node = node[char]
            else:
                return False
        return "$" in node


    def search(self, word: str) -> bool:
            return self.search_node(word, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)