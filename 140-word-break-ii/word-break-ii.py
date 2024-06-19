class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        n = len(s)
        res = []

        # helper
        def backtrack(slate, start):
            if start >= n:
                res.append(" ".join(slate[:]))
                return


            for end in range(start, n):
                if s[start:end+1] in wordDict:
                    # print(s[start:end+1])
                    slate.append(s[start:end+1])
                    backtrack(slate, end+1)
                    slate.pop()
        
        backtrack([],0)
        return res
        