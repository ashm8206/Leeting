class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        up = 1
        pre_max_up = 0
        res = 0

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                up+=1
            else:
                pre_max_up = up
                up = 1
            
            res = max(res, up//2, min(pre_max_up, up))

            # Why up//2?
            #  Well we need to check if curr subarray 
            # can be halved to get the result.

            # Why use min(pre_max_up, up)? 
            # This ensures that the result reflects the smallest increasing subarray before and after a break in the sequence.
        return res >= k