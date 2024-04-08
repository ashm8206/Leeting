class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count = 0
        maxCount = -10**5

        for num in nums:
            if num==1:
                count+=1
            else:
                # here you wait for a boundary of zero to call the maxCount function
                maxCount = max(count, maxCount)
                count = 0

        # What if you reach the end, without encounteringa boundary ?\
        # You do max()  --> with the count variable.
        return max(maxCount,count)


        