class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.next = [None] * 26  # For lowercase English letters

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not node.next[idx]:
                node.next[idx] = TrieNode()
            node = node.next[idx]
        node.isEnd = True

class Solution:
    def __init__(self):
        self.trie = Trie()
        self.dp = []
        self.n = 0

    def dfs(self, s: str, start: int):
        # If we have reached the end of the string, return a list containing an empty string
        if start == self.n:
            return [""]
        
        # If the solution is already computed for this start index, return the stored result
        if self.dp[start]:
            return self.dp[start]

        ans = []
        node = self.trie.root
        current_prefix = ""

        # Iterate through the string from the current start index
        for i in range(start, self.n):
            idx = ord(s[i]) - ord('a')
            # If the current character is not in the Trie, break the loop
            if not node.next[idx]:
                break

            node = node.next[idx]
            current_prefix += s[i]

            # If we find a valid word (end of a word in the Trie)
            if node.isEnd:
                rest = self.dfs(s, i + 1)
                for r in rest:
                    ans.append(current_prefix + (" " if r else "") + r)

        # Store the result for this start index in dp
        self.dp[start] = ans
        return ans

    def wordBreak(self, s: str, wordDict: list) -> list:
        self.n = len(s)
        
        # Insert all words from wordDict into the Trie
        for word in wordDict:
            self.trie.insert(word)

        # Initialize dp for memoization
        self.dp = [[] for _ in range(self.n + 1)]

        # Start the dfs from index 0 of the string
        return self.dfs(s, 0)





        # Option 2: Memoization

        # res = []
        # n = len(s)
        # wordDict = set(wordDict)

        # memo = {} # Option 2

        # def helper(idx):

        #     if idx == n:
        #         return [""] # has to be this

        #     if idx in memo:
        #         return memo[idx]

        #     results = []
        #     for i in range(idx,n):
        #         current_word = s[idx:i+1]
        #         if current_word in wordDict:
        #             for next_word in helper(i+1):
        #                 results.append(current_word + (
        #                     " "+ next_word if next_word else ""
        #                 ))
        #     memo[idx] = results
        #     return memo[idx]

        # return helper(0)
    

        

        # OPTION 1: EASIEST: BACKTRACKING
        # n = len(s)
        # res = []
        # wordDict = set(wordDict)


        # # helper
        # def backtrack(slate, start):
        #     if start >= n:
        #         res.append(" ".join(slate[:]))
        #         return


        #     for end in range(start, n):
        #         if s[start:end+1] in wordDict:
        #             # print(s[start:end+1])
        #             slate.append(s[start:end+1])
        #             backtrack(slate, end+1)
        #             slate.pop()
        
        # backtrack([],0)
        # return res
        