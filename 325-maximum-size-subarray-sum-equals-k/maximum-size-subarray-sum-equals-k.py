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

            # if curr_sum == k:
            #     maxLen  = max(maxLen, i+1)
                # maxLen = i+1

            if curr_sum - k in hmap.keys():
                maxLen = max(maxLen, i-hmap[curr_sum - k])
            
            if curr_sum not in hmap.keys():
                # seeing for the first time
                hmap[curr_sum] = i  # Don't place it in every iteration

            # print(curr_sum, curr_sum-k, maxLen)
    
        return maxLen
        # 1,-4, 1 = 
        
        


        
