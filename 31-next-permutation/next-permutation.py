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
        # https://leetcode.com/problems/next-permutation/solutions/3473399/beats-100-full-explanation-in-steps-by-r-mdqu


        # [1, 2, 5, 4, 3]
        #  break pt is 2
    
        # [1, 3, 5, 4, 2]
        # smallest num (viz is the first num from right)   > 2

        # Now to get the permuation, reverse from swap pt
        # to find next smallest permuation

        # [1, 3, 2, 5, 4]
        n = len(nums)
        breakpt = n - 1

        while breakpt > 0 and nums[breakpt-1] >= nums[breakpt]:
            breakpt-=1 
            # find the first number that is nums[i] < nums[i+1]
            # from end

        
        if breakpt==0: 
            # no next permuation exists for a descending array
            # move to start
            nums.reverse()
            return

    
        # find swap index
        j =  n - 1

        # smallest num (viz is the first num from right)   > breakpt
        while j > 0 and nums[breakpt-1] >= nums[j]: 
            j-=1
        
        # Swap
        nums[breakpt-1], nums[j] = nums[j], nums[breakpt-1]

        # Reverse the subsequence to the right of breakpt-1
        l = breakpt
        r = n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1

        