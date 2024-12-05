class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)

        mask = n
        xor = 0

        for i in range(n):
            mask^=i
            xor^=nums[i]
        
        return xor^mask
           
                # this is the dup, first time you get it set it
            
          
        