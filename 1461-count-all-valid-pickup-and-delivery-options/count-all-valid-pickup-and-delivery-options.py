class Solution:
     def countOrders(self, n: int) -> int:
        ans, MOD = 1, 10**9 + 7
        for i in range(2, n+1):
            spaceNum = (i - 1) * 2 + 1
            ans *= spaceNum * (spaceNum + 1) // 2
            ans %= MOD
        return ans
        