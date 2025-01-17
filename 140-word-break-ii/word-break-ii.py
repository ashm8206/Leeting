class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        res = []
        n = len(s)
        wordDict = set(wordDict)

        def helper(idx, slate):

            if idx == n:
                res.append(" ".join(slate[:]))
                return
            
            for i in range(idx,n):
                if s[idx:i+1] in wordDict:
                    slate.append(s[idx:i+1])
                    helper(i+1, slate)
                    slate.pop()
                    
        helper(0, [])
        return res
        
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
        