class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}
        n = len(piles)

        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        for i in range(n-2, -1, -1):
            suffix_sum[i] = piles[i] + suffix_sum[i + 1]
        
        def helper(i,m):
            if i >=n:
                return 0

            if (i,m) in dp:
                return dp[(i,m)]

            ans = 0
            for x in range(1, 2*m+1):
                if i + x <= n:
                    ans = max(ans, suffix_sum[i] - helper(i+x,max(x,m)))
            dp[(i,m)] = ans
            return dp[(i,m)]
        return helper(0,1)
