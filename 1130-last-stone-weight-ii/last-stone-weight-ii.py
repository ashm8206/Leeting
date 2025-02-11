class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # https://leetcode.com/problems/last-stone-weight-ii/solutions/295209/stupidly-easy-python-brute-force-memorization

   
        stoneSum = sum(stones)
        target = math.ceil(stoneSum /2) 
        # target = (stoneSum + 1) // 2

        @lru_cache(maxsize=None)
        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (stoneSum - total)) # (y-x)
            return min(dfs(i + 1, total), dfs(i + 1, total + stones[i]))

        return dfs(0, 0)