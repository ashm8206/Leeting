from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        ''' 
        WHY ITS NOT VANILLA Sliding window:

        - When oddCount < k → expanding helps
        - When oddCount > k → shrinking helps
        - When oddCount == k → expanding breaks it, shrinking breaks it
        '''  # NO single monotonic rule we can use greedily

        # def atMost(nums, k):
        #     l = 0
        #     oddCount = 0
        #     count = 0

        #     for r in range(len(nums)):
        #         oddCount += nums[r] % 2

        #         while oddCount > k:
        #             oddCount -= nums[l] % 2
        #             l += 1

        #         count += r - l + 1

        #     return count
        # return atMost(nums, k) - atMost(nums, k-1)



        # def numberOfSubarrays(nums, k):
        l_far = 0
        l_near = 0
        oddCount = 0
        res = 0

        for r in range(len(nums)):
            # Expand window
            if nums[r] % 2 == 1:
                oddCount += 1

            # If we exceed k odds, move l_far
            while oddCount > k:
                if nums[l_far] % 2 == 1:
                    oddCount -= 1
                l_far += 1
                l_near = l_far   # reset l_near when we lose an odd

            # If we have exactly k odds, shrink l_near over evens
            if oddCount == k:
                while nums[l_near] % 2 == 0:
                    l_near += 1
                res += (l_near - l_far + 1)

        return res




        # prefixMap = {0:1}
        # count = 0

        # curr_sum = 0

        # #  Subarray sum equals k
        # #       Keep adding curr_sum to Map with Unique counts

        # #    1. We are looking for curr_sum[j] - curr_sum[i] = k
        #         #   or curr[j]-k = curr[i], we are lookin for curr[i]

        # #    if we get curr_sum-k in prefixMap,
        #         # we found a some previous value curr[i]... curr[j](curr_sum)
        #         # that can be combined with curr_sum
            
        # #  Subarray has k odd numbers 
        # #  We can model this as nums[i] even = 0 and nums[i] = 1
        
        # for num in nums:
            
        #     curr_sum+= num%2 # odd the 1, even 0
            
        #     if curr_sum - k  in prefixMap:
        #         count+= prefixMap[curr_sum - k ]
           
        #     prefixMap[curr_sum] = prefixMap.get(curr_sum, 0) + 1
        # return count