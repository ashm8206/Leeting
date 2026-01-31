class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # a | b and b | c then a | c

        # Sorted: You only need to check nums[j] % nums[i] == 0.
        # Unsorted: You would have to check both nums[i] % nums[j] == 0 and nums[j] % nums[i] == 0
        n = len(nums)
        dp = [ 1 for i in range(n)]
        nums.sort()

        
        parent = [0  for i in range(n)]
        maxLen = 1
        lastIndex = 0

        for i in range(n):
            parent[i] = i
            for j in range(0, i):
                if nums[i]%nums[j]==0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        parent[i] = j

            if maxLen < dp[i]:
                maxLen = dp[i]
                lastIndex = i
        
        ans = []
        
        i = lastIndex

        while parent[i]!=i:
            ans.append(nums[i])
            i = parent[i]
        
        # Append the last element
        ans.append(nums[i])
        print(parent, dp, i)
        return ans[::-1]
