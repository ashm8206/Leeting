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

        for i, char in enumerate(word):
            
            if char not in node:
                if char == ".":
                    for key in node.keys():
                        """
                        For every key at this level, excluding "$" ending char
                        as it is not a valid char in input, but a stub created 
                        by us.

                        for every key, pass their mapping node[key] and 
                        the word[i+1: ], as it is the next char after "."

                        Start a new search(word, node[key]) for all key
                        mappings at this level, if any of them match return True

                        if None of they match, return True

                        """
                        if key!='$' and self.search_node(word[i+1:],node[key]):
                            return True
                return False

            else:
                node = node[char]
           
        return "$" in node


    def search(self, word: str) -> bool:
            return self.search_node(word, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)