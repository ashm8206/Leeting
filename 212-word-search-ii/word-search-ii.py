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

    # Instead of N * 3^L for every word

    # we match only the prefixes from the wordList
    # if we find the entire word . is_end = True
    #                 we append tto the result list

    def dfs(self, board, node, i, j, path, res):

        if node.isWord:
            res.append(path)
            node.isWord = False

         # set this to false. to avoid duplicates
         # don't return as new word with matched as prefix might be present
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return 
        
        
        letter = board[i][j]
        if letter in node.children:
            node = node.children[letter]
        else:
            # abandon this path, Prefix not found in Trie
            return
        
        board[i][j] = "#"
        # ^^  we modify the  board instead of using a visited array

        # for nr, nc in [(i+1, j), (i-1, j),(i, j-1),(i, j+1)]:
        #     if nr < 0 or nr >= len(board) or nc < 0 or nc >= len(board[0]):
        #         continue 
        #     self.dfs(board, node, nr, nc, path+letter, res)
        # it skips the next iteration

        self.dfs(board, node, i+1, j, path+letter, res)
        self.dfs(board, node, i-1, j, path+letter, res)
        self.dfs(board, node, i, j-1, path+letter, res)
        self.dfs(board, node, i, j+1, path+letter, res)

        board[i][j] = letter

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # only find those start words in the trie
        # no need to start from every r.c

       
        trie = Trie()

        for w in words:
            trie.insert(w)

        node = trie.root
        res = []
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in node.children:
                    self.dfs(board, node, i, j, "", res)
        return res