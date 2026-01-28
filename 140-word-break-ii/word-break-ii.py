class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isEnd = False
        

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

class Solution:
    
    def wordBreak(self, s: str, wordDict: list) -> list:
    # #     n = len(s)
    # #     trie = Trie()
        
    # #     # Insert all words from wordDict into the Trie
    # #     for word in wordDict:
    # #         trie.insert(word)

    # #     dp = {}
    # #     def dfs(s, start):
    # #         # End, return list containing empty string
    # #         if start == n:
    # #             return [""]
            
    
    # #         if start in dp:
    # #             return dp[start]

    # #         ans = []
    # #         node = trie.root
    # #         current_prefix = ""

            
    # #         for i in range(start, n):
    # #             char = s[i]
    # #             # If char not not in the Trie, break the loop
    # #             if char not in node.children:
    # #                 break

    # #             node = node.children[char]
    # #             current_prefix += s[i]

    # #             # If we find a valid word (end of a word in the Trie)
    # #             if node.isEnd:
    # #                 rest = dfs(s, i + 1)
    # #                 for r in rest:
    # #                     ans.append(current_prefix + (" " if r else "") + r)

    # #         # Store the result for this start index in dp
    # #         dp[start] = ans
    # #         return ans


    #     return dfs(s,0)
        

        # OPTION 1: EASIEST: BACKTRACKING
        n = len(s)
        res = []  
        wordDict = set(wordDict)


        # helper
        def backtrack(start, slate):
            if start == n:
                res.append(" ".join(slate[:]))
                return


            for end in range(start, n):
                curr_word = s[start:end+1]
                if curr_word in wordDict:
                    slate.append(curr_word)
                    backtrack(end+1, slate)
                    slate.pop()
        
        backtrack(0,[])
        return res

        # Option 3: Memoization

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
    
        