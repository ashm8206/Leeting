class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while nums[0]!=nums[nums[0]]:
            # nums[nums[0]], nums[0] = nums[0], nums[nums[0]]

            # This one doesnt work: 
            # nums[0], nums[nums[0]] = nums[nums[0]], nums[0]

            temp = nums[nums[0]]
            nums[nums[0]] = nums[0] # put whats in nums[0] at the right plae
            nums[0] = temp

        return nums[0]
        