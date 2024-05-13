class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        # sum[j] == sum[i] + k then sum[j]-sum[i] = k
        
        hmap = {0:1}
        curr_sum = 0
        n = len(nums)
        res = 0

        for i in range(n):
            curr_sum += nums[i]
            diff = curr_sum - goal

            res+= hmap.get(diff, 0)

            hmap[curr_sum] = hmap.get(curr_sum, 0) + 1

        return res
