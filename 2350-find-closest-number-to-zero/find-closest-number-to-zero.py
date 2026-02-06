class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # return mininum abs number 
        # if equivdistnace return larger
        return min(nums, key=lambda i:(abs(i),-i))