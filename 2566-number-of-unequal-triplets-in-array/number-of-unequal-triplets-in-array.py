class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n-2):
            for j in range(i+1,n-1):
                if nums[j]!=nums[i]:
                    for k in range(j+1,n):
                        if nums[k]!=nums[j] and nums[k]!=nums[i]:
                            count+=1
        return count