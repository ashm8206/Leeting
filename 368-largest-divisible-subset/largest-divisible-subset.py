class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # a | b and b | c then a | c

        n = len(nums)
        dp = [ 1 for i in range(n)]
        nums.sort()
        prev = [-1  for i in range(n)]
        maxLen = 1
        reverseStart = -1

        for i in range(n):
            for j in range(0, i):
                if nums[i]%nums[j]==0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        prev[i] = j

            if maxLen < dp[i]:
                maxLen = dp[i]
                reverseStart = i
        
        ans = []
        
        if reverseStart!=-1:
            nextIdx = reverseStart
            while nextIdx!=-1:
                ans.append(nums[nextIdx])
                nextIdx = prev[nextIdx]
            return ans[::-1]
        else:
            return [nums[0]]
