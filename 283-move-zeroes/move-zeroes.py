class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # j moves from i ---> n
        # and finds a new Non-zero to write to i
        # i moves chronologically
        # j also moves chronological to find next Non-Zero
        # This ensures that order is maintained
        # lastZeroFoundAt = 0
        # for fast in range(n):
        #     # j = i
        #     # while j < n and nums[j]==0:
        #     #     j+=1
        #     # if j < n  and nums[j]!=0:
        #     #     nums[i], nums[j] = nums[j], nums[i]
        #     if nums[fast]!=0 and nums[lastZeroFoundAt]==0:
        #         nums[lastZeroFoundAt], nums[fast] = nums[fast], nums[lastZeroFoundAt]

        #     if nums[lastZeroFoundAt]!= 0:
        #         lastZeroFoundAt+=1

        #Slow ptr keeps track of next position to place the element
        # Fast Pointer parse the elements


        # Method II
        # Similar to Remove Element
        # Overwrite elements + fill with zeroes
        nextIndex = 0

        for runner in range(n):
            if nums[runner]!=0:
                nums[nextIndex] = nums[runner]
                nextIndex += 1

        for i in range(nextIndex, n):
            nums[i]=0
        return nums

    



        

        