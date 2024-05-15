class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        hmap = {0:-1}
        curr_sum = 0
        res = 0
        maxLen = -10**9

        for i in range(n):
            curr_sum += nums[i]

            if curr_sum == k:
                maxLen  = max(maxLen, i+1)
                # maxLen = i+1

            if curr_sum - k in hmap.keys():
                maxLen = max(maxLen, i-hmap[curr_sum - k])
            
            if curr_sum not in hmap.keys():
                # seeing for the first time
                hmap[curr_sum] = i

            # print(hmap)
        return maxLen if maxLen > -10**9 else 0
            # -2, -3, 1, 2
        


        
