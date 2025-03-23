class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        # def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Handle simple edge cases
        if n == 1:
            return 1
        
        # Find longest prefix that is strictly increasing
        left = 0
        while left + 1 < n and nums[left] < nums[left + 1]:
            left += 1

         # If the entire array is already strictly increasing
        if left == n - 1:
            return (n * (n + 1)) // 2
            
        # Find longest suffix that is strictly increasing
        right = n - 1
        while left < right  and nums[right - 1] < nums[right]:
            right -= 1
            
       
            
        # Count subarrays to remove
        # remove each individual elements + remove entire array
        result = n + 1 + (left+1 - right) # overlap
        i = 0

        while i <=left and right < n:
            if nums[i] < nums[right]:
                result += n - right
                # len == [right-i-1]
                #{len subarray that if removed will: make result sorted}         
                if i + 1 < n and nums[i] < nums[i + 1]:
                    i+=1
                else:
                    break
            else:
                right+=1
        return result

        
        # # Count valid removals when connecting prefix and suffix
        # while left <= left and right < n:
        #     if nums[left] < nums[right]:
        #         result += n - right
                
        #         if left < n - 1 and nums[left] < nums[left + 1]:
        #             left += 1
        #         else:
        #             break
        #     else:
        #         right += 1
                
        # return result
