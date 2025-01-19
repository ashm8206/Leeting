class Solution:
    def minimumScore(self, s: str, t: str) -> int:

        ss, st = len(s), len(t)
        k = st - 1
        dp = [-1] * st
        
        # Step 1: Fill dp array by tracking the positions of matching characters from the end
        for i in range(ss - 1, -1, -1):
            if k >= 0 and s[i] == t[k]:
                dp[k] = i
                k -= 1
        
        # Step 2: Find the minimum score
        res = k + 1
        if res == 0:
            return 0
            
        j = 0
        for i in range(ss):
            if j < st and s[i] == t[j]:
                while k < st and dp[k] <= i:
                    k += 1
                res = min(res, k - (j + 1))
                j += 1
        
        return res
