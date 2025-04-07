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
                    #The recursive call helper(i + x, max(x, m)) represents the optimal play for Bob, who tries to minimize Alice's future gain.

                # Alice's stones = total remaining stones minus Bob's optimal stones
                # total remaining stones is suffix[i]


                # The next pile for bob is at index (i+x)
                # Alice takes 1st x Pile
                #  i i+1 , i+ 2...i+x - 1





            dp[(i,m)] = ans
            return dp[(i,m)]
        return helper(0,1) 
        # (i,m) : maxStones Alice collects starting at index i, 
        # with first X = 1
