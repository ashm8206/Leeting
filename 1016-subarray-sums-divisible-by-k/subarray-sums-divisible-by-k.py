class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0

        hmap = {0: 1} # hmap of prefix sum seen so sofar, with their counts
        curr_sum = 0
        # diff = 0 # two sum
        
        for i in range(n):
            curr_sum = (curr_sum + nums[i]) % k

            # if curr_sum in hmap.keys():
            #     res += hmap[prefix_mod]
            
            res += hmap.get(curr_sum,0) # number of times it occured before
            
            hmap[curr_sum] = hmap.get(curr_sum, 0) + 1
        
        return res