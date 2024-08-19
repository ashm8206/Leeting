class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordDict = set(wordDict)
        n = len(s)

        @lru_cache(maxsize=None)
        def helper(start, s):
            if start >= n:
                return True
                
            for end in range(start, n+1):
             
                if s[start: end] in wordDict:
              
                    if helper(end, s):
                        return True
            return False

        return helper(0, s)