class TrieNode():
    def __init__(self):
        self.children = dict()
        self.isWord = False
    
class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.isWord = True

class Solution:

    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return 
        
        letter = board[i][j]
        node = node.children.get(letter)

        if not node:
            return
        
        board[i][j] = "#"
        self.dfs(board, node, i+1, j, path+letter, res)
        self.dfs(board, node, i-1, j, path+letter, res)
        self.dfs(board, node, i, j-1, path+letter, res)
        self.dfs(board, node, i, j+1, path+letter, res)
        board[i][j] = letter

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # only find those start words in the trie
        # no need to start from every r.c

        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res