class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        total_sum = sum(nums)

        target = total_sum % p
        if target == 0:
            # no removal required, return empty subarray
            return 0
        # we need to remove a subarray that equals target

        mod_map = {0:-1} # mod map that stores indexes
        n = len(nums)
        min_len = n 
        # curr_sumj - curr_sumi % p == target
        # curr_sumj - target % p = curr_sumj

        curr_sum = 0
        for i in range(n):
            curr_sum = (curr_sum + nums[i])%p
            # find the complement
            needed = (curr_sum - target + p ) % p

            # diff = target-curr_sum
            # if diff in array

            if needed in mod_map:
                min_len = min(min_len, i - mod_map[needed]) 
                # subarray[neededIdx: i] not including i

            mod_map[curr_sum] = i

        return -1 if min_len == n else min_len