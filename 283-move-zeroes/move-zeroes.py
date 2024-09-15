class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # Slow ptr keeps track of next position to place the element
        # Fast Pointer parse the elements

        # All elements before the slow pointer (lastNonZeroFoundAt) are non-zeroes.
        # All elements between slow ptr .... fast ptr may contain Zeroes.
        #  They may contain Zeroes if there were indeed Zeroes in the array
        #  If there were no zeros, they will never show up
      
        lastZeroFoundAt = 0
        for fast in range(n): # reader Pointer

            if nums[fast]!=0:
                nums[lastZeroFoundAt], nums[fast] = nums[fast], nums[lastZeroFoundAt]

                # you cant guarantee that "lastZeroFoundAt" will alwyas contain zero, but when  you are copying, a non-zero into this location
                # Doesn't hurt to copy whatever is in lastzero to the "fast" ptrs location
                # Eventually, if there are zeroes in the array. 
                # We are bound to reach them as InsertIdx progresses, 
                # as they were never copied, previously.
                # It is these "Zeros" that will be copied into non-zero future "fast" positions
                lastZeroFoundAt+=1


 


        # Method II
        # Similar to Remove Element
        # Overwrite elements + fill with zeroes
        # nextIndex = 0

        # for runner in range(n):
        #     if nums[runner]!=0:
        #         nums[nextIndex] = nums[runner]
        #         nextIndex += 1

        # for i in range(nextIndex, n):
        #     nums[i]=0
        # return nums

    



        

        