class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0

        hmap = {0: 1} # hmap of prefix sum seen so sofar, with their counts
        curr_sum = 0
        
        for i in range(n):
            curr_sum = (curr_sum + nums[i]) % k
            
            # No need for Difff
            # As
            # prefixSum[i] % k == prefixSum[j] % k

            res += hmap.get(curr_sum,0) # number of times it occured before
            
            hmap[curr_sum] = hmap.get(curr_sum, 0) + 1

        return res