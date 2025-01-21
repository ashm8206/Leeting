class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        # Test case 2: [3,2,1]
        # Such an Arrangement is not possible : 
        # If such arrangement is not possible, the array must be rearranged as the lowest possible order 
        (i.e., sorted in ascending order)
        """

        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1

        if i == 0:   # nums are in descending order
            nums.reverse()
            return 
        
        # find the last "ascending" position
        while nums[j] <= nums[i-1]:
            j -= 1

        nums[i-1], nums[j] = nums[j], nums[i-1]  
        l, r = i, len(nums)-1  # reverse the second part

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 
            r -= 1

        # [1,2,3,6,5]
        #  Step I :
        #       find where ther number decrease from end [6,5]--> largest arrangement
        #       3 if the place where changes can be made
        # Step II:
        #       Swap 3, with its next largets from the back to get just Next Greater Permuation
        #       [1,2,5,6,3]
        # Step III:
        # to make just next greater, we need to reverse the elements till swap position
        # [1,2,5,6,3]. --> [1,2,5,3,6].

        # n = len(nums)
        # i = n - 2

        # # Step 1: Find First Decreasing element, 
        # while i >=0 and nums[i] >= nums[i+1]:
        #     i-=1
        
        # swap = i
        # # incase of Descending it will be -ve 

        # if i>=0:
        #     indexVal =  nums[i]
        #     i = n - 1

        #     # STEP 2: Find its next greater value that the decreasing element  ans Swap

        #     while i>=0 and nums[i]<=indexVal:
        #         i-=1
        
        #     #Element found now, swap it

        #     nums[swap], nums[i] = nums[i], nums[swap]

        #     # print(nums)
        #     # print(swap, n-1)
    
        # start = swap + 1
        # end = n - 1

        # while start < end:
        #     nums[start], nums[end] = nums[end], nums[start]
        #     start+=1
        #     end-=1

        # return nums



