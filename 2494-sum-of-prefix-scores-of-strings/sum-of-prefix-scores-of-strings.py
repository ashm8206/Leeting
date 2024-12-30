class TrieNode:
    def __init__(self):
        self.children = dict()
        self.score = 0

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root

        for i, c in enumerate(word):
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.score +=1

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # store sum at each node.
        # as you search through each word add the score at each level to get ans[i]  
        
        for word in words:
            self.add_word(word)

        ans = [0] * len(words)

        for i, word in enumerate(words):
            node = self.root
            for c in word:
                if c in node.children:
                    ans[i] += node.children[c].score
                    node = node.children[c]
        return ans

