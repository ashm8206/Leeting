class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        hmap = {0:-1} 
        # it does make sense to initialize this.
        # Why ?
         # Since we are morphing this problem int subarray k where k= 0
        # we will have to store the key here
        # [(0,1), (0,1, 1, 0)]
        # longest subarray will be rooted at from start

        # For shortest, It would be a different story, 
        # we wouldnt want to initialize this value.
    
        curr_sum = 0
        res = 0
        maxLen = 0 

        # currSum[j] - previous[i] = k
        # currSum[j] - k  = previous[i] , then we found a subarray

        for i in range(n):
            curr_sum += nums[i]
            diff = curr_sum - k

            if diff in hmap.keys():
                maxLen = max(maxLen, i-hmap[diff])
                # between hmap[diff] = idx ..... i : (idx,i] 
                # not including idx, array_sum == k
                # Why?
                # prefix_sum[:i] uptil i= curr_sum
                # we get this in O(1)
                # j = hmap[curr_sum - k]

                # prefix[:j] uptil j = curr_sum - k
                # 0...........j........ i
                #   curr_sum-k   
                # ............curr_sum......
                # sumi - sumj = curr_sum - [curr_sum - k] =  k 
                # R-L : exlue 1 index, in this case its J
                # sum[j+1...i]  = k)
            
            if curr_sum not in hmap.keys():
                # seeing for the first time
                hmap[curr_sum] = i  
                # Don't place it in every iteration
                # we want maximium size

        return maxLen

        #  if sum[i]−sum[j]=k, 
        #  the sum of elements lying between indices i and j is k.

        # If prefixSum - k exists in indices, that means there is a subarray with sum k ending at the current i. 
        # The length will be i - indices[prefixSum - k] --> dont include  
        # start index
       
        
        


        
