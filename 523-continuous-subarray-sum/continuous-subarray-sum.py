class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hmap = {0: -1}
        curr_sum = 0
        n = len(nums)

        for i in range(n):
            curr_sum = (curr_sum + nums[i]) % k

            
            if curr_sum in hmap.keys():
                if i - hmap[curr_sum] > 1:
                    return True
            else:
                hmap[curr_sum] = i
        return False

        