class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        # def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Handle simple edge cases
        if n == 1:
            return 1
        # if n == 2:
        #     return 3
            
        # Find longest prefix that is strictly increasing
        left = 0
        while left < n - 1 and nums[left] < nums[left + 1]:
            left += 1
            
        # Find longest suffix that is strictly increasing
        right = n - 1
        while right > 0 and nums[right] > nums[right - 1]:
            right -= 1
            
        # If the entire array is already strictly increasing
        if left >= right:
            return (n * (n + 1)) // 2
            
        # Count subarrays to remove
        result = n + left - right + 2
        left = 0
        
        # Count valid removals when connecting prefix and suffix
        while left <= left and right < n:
            if nums[left] < nums[right]:
                result += n - right
                
                if left < n - 1 and nums[left] < nums[left + 1]:
                    left += 1
                else:
                    break
            else:
                right += 1
                
        return result
