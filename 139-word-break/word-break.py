class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:


        wordDict = set(wordDict)
        n = len(s)

        memo = {}

        # def helper(start):

        #     if start >= n:
        #         return True

        #     for end in range(start+1, n+1):
        #         curr_str = s[start:end] # end goes til n slice +1 in py
        #         if curr_str in wordDict:
        #             if helper(end): # start where it ended
        #                 return True
        #     return False
        # return helper(0)


        def helper(start):

            if start >= n:
                return True

            if start in memo:
                return memo[start]

            for end in range(start+1, n+1):
                curr_str = s[start:end] # end goes til n slice +1 in py
                if curr_str in wordDict:
                    if helper(end):
                        memo[start] = True
                        return True
            memo[start] = False
            return False
        helper(0)
        return memo[0]


       
        # # Time-Complexity: O(n⋅m⋅k)
        # # Space: O(n)


        # Neetcode
        #  n = len(s)

        # dp = [False]*(n+1)
        # dp[n] = True

        # for i in range(n, -1, -1):
        #     for word in wordDict:
        #         if i+len(word) <= n and s[i : i+ len(word)]==word:
        #             dp[i] = dp[i+ len(word)]
        #         if dp[i]:
        #             break
        # return dp[0]