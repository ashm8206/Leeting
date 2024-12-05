class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0

        while i < n:
            j = nums[i] - 1
            if nums[i] > 0 and nums[i]<=n and nums[i]!=nums[j]:
                # place whatever is in nums[0] at its correct index
                nums[i], nums[j] = nums[j], nums[i]

                #Side Note
                # always evaluate Right to Left
                # what is nums[i] goes to nums[j] first
                # nums[j] goes to nums[i]
            else:
                i+=1 
            # out of range or negative number or the number in correct spot

        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1

        