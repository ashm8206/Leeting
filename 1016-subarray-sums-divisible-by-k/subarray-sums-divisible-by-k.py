class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0

        # curr_sum = 0 %k  --> 0

        hmap = {0: 1} # hmap of prefix sum seen so sofar, with their counts
       
        # remainder = 0
        # curr_sum = 0
        # for i in range(n):
        #     # remainder = (remainder + nums[i]) % k
            
        #     # key = curr_sum % k

        #     curr_sum +=nums[i]
        #     remainder = curr_sum % k

        #     # No need for Difff
        #     # As
        #     # prefixSum[i] % k == prefixSum[j] % k
        #     #  r1 = r0

        #     res += hmap.get(remainder,0) # number of times it occured before
            
        #     hmap[remainder] = hmap.get(remainder, 0) + 1

        # return res

    
        curr_sum = 0
        for num in nums:
            
            curr_sum += num

            if curr_sum%k in hmap:
                
                res+= hmap.get((curr_sum%k), 0)
            else:
                res+= hmap.get(k + (curr_sum%k), 0)

            hmap[curr_sum %k] =  hmap.get(curr_sum%k, 0) + 1

        return res
       
        