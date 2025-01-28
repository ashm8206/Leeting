class TrieNode:
    def __init__(self, atMost=3):
        self.children = defaultdict(dict)
        self.wordList = []

class Trie:
    def __init__(self):
        self.root = TrieNode(atMost=3)
    
    def add(self, word):
        root = self.root
        
        for ch in word:
            if ch not in root.children:
                root.children[ch] = TrieNode()
            root = root.children[ch]

            root.wordList.append(word)
            # root.wordList.sort()
            # if len(root.wordList) > 3:
            #    root.wordList.pop()

        

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        trie = Trie()
        for product in products:
            trie.add(product)
        
        curr = trie.root
        res = []
        for ch in searchWord:
            if ch in curr.children:
                curr = curr.children[ch]
                res.append(sorted(curr.wordList)[:3])
            else:
                curr.children = {}
                res.append([])
        # searching for prefix
        #  m, mo, mou --> repeative 
        # search once
        return res
   


