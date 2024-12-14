class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefixMap = {0:1}
        count = 0

        curr_sum = 0

        #  Subarray sum equals k
        #       Keep adding curr_sum to Map with Unique counts

        #    1. We are looking for curr_sum[j] - curr_sum[i] = k
                #   or curr[j]-k = curr[i], we are lookin for curr[i]

        #    if we get curr_sum-k in prefixMap,
                # we found a some previous value curr[i]... curr[j](curr_sum)
                # that can be combined with curr_sum
            
        #  Subarray has k odd numbers 
        #  We can model this as nums[i] even = 0 and nums[i] = 1
        
        for num in nums:
            
            curr_sum+= num%2
            
            if curr_sum - k  in prefixMap:
                count+= prefixMap[curr_sum - k ]
           
            prefixMap[curr_sum] = prefixMap.get(curr_sum, 0) + 1
        return count