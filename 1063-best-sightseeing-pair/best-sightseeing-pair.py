class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # when you have two Points.
        # fix one
        # try to find another pair:
            # Sliding
            # hashmap/ prefix map
        ans = float("-inf")

        n = len(values)

        dp = [0]*n
        dp[0]= 0
        for j in range(1,n):
            dp[j] = max(dp[j-1], values[j-1]+j-1) # getting left value
            ans = max(ans,dp[j] + values[j] - j)
        return ans