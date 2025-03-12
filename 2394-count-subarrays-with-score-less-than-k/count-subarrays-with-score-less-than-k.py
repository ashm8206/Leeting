class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
       
        ans = 0
        left = 0
        curr_sum = 0
        for right, num in enumerate(nums):
            curr_sum+=num

            while curr_sum *(right-left+1)>=k:
                curr_sum-=nums[left]
                left+=1
            ans += (right-left+1)
        return ans