class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # nums = [1,1,0,0,1,1,0,1,1]
        # sum =  [1,2,1,0,1,2,1,2,3]

        hmap = {0:-1}
        maxLen = -10**9
        curr_sum = 0
        n = len(nums)


        for i in range(n):
            curr_sum += -1 if nums[i]==0 else nums[i]

            if curr_sum in hmap.keys():
                maxLen = max(maxLen, i-hmap[curr_sum])
            else:
                hmap[curr_sum] = i

        return maxLen if maxLen > -10**9 else 0




        
        
    