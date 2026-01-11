class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        pf = [0]*(n+1)
        count = 0

        for i in range(n):
            pf[i+1] = pf[i] + nums[i]
        
        for i in range(n-1):
            left = pf[i+1]
            right = pf[n] - pf[i+1]
            # print(left, right)
            if (right - left)%2 == 0:
                count+=1
        return count