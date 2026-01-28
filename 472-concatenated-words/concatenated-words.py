class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        originalSet = set(words)
        memo = {}
        def helper(word):

            if word in memo:
                return memo[word]

            n = len(word)

            res = False
            for split in range(n):
                # atleast 2
                prefix = word[:split+1]
                suffix = word[split+1:]
                
                
                if prefix in originalSet:
                    if suffix in originalSet or helper(suffix): 
                        # to divide further
                        res = True
                        break
            memo[word] = res
            return memo[word]

        res = []

        for word in words:
            if helper(word):
                res.append(word)
        return res