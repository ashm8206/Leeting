class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        
        left = 0
        total = sum(nums)
        n = len(nums)
        countValid = 0

        for i in range(n):
            left+=nums[i]
            total-=nums[i]

            if nums[i]==0:
                if left == total:
                    # going in either direct is valid
                    countValid+=2
                elif abs(left - total) == 1:
                    # go in 1 direction
                    countValid+=1
        
        return countValid

                