class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        originalSet = set(words)
        @lru_cache()
        def helper(word):
            
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in originalSet:
                    if suffix in originalSet or helper(suffix):
                            return True
            return False
              

        res = []

        for word in words:
            if helper(word):
                res.append(word)
        return res