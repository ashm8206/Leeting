class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        total_sum = sum(nums)

        target = total_sum % p
        if target == 0:
            # no removal required, return empty subarray
            return 0
        # we need to remove a subarray that equals target, viz remainder

        mod_map = {0:-1} # Length, store index
        n = len(nums)
        minLen = n 


        # (curr_sumj - curr_sumi) % p == target
        #  curr_sumi%p  = (curr_sumj - target) % p
        # curr_sumi%p  = (curr_sumj - target + p) % p --> [0..p-1]
        # add p to ensure positive result
        

        curr_sum = 0
        for i in range(n):
            curr_sum+= nums[i]
            curr_sumj =  curr_sum%p
            # find the complement
            needed = (curr_sumj - target + p )% p


            if needed in mod_map:
                minLen = min(minLen, i - mod_map[needed]) 
                # subarray[neededIdx: i] not including neededIdx
                # sums to the target 

            # smallest_indx, so update mod everytime
            mod_map[curr_sumj] = i

        return -1 if minLen == n else minLen