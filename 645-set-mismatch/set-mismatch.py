class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        ans = [-1,-1]
        n = len(nums)

        mask = 0
        xor = 0

        for i in range(n):
            mask^=i+1
            xor^=abs(nums[i])

            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                ans[0] = idx + 1 
                # this is the dup, first time you get it set it
          
            nums[idx] = -nums[idx]

        ans[1] = xor ^ mask ^ ans[0]
        return ans


        