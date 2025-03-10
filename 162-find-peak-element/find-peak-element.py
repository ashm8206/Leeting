class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
       
        # Greedy approach
        # -inf [1, 2, 3, 1] -inf

        # A peak element is an element that is strictly greater than its neighbors

        #  the greedy strategy is to go toward the greater numbers

        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                # go where the greater element is
                r = mid
            else:
                # = doesnt tell us anything
                l = mid + 1
        return l

        

        n = len(nums)

        l = 0 
        r = n - 1

        while l <=r : # this will handle 1 element case
            mid = (l+r)//2

            if mid+1 < n and nums[mid] <= nums[mid+1]:
                l = mid + 1
            elif mid-1 >=0 and nums[mid-1] >= nums[mid]:
                r = mid - 1
            else:
                # arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]
                return mid
        
        # check the edges, and return the index
        if nums[0] > nums[1]:
            return  0
        elif nums[n-1] > nums[n-2]:
            return n-1
        
        

