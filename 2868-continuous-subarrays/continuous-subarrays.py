class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left = 0
        right = 0
        count = 0

        # [1,2,3] = 1. vs index
        #  [1,2], [2,3] = 2
        #  [1]*3 = 3


        minNum = nums[0]
        maxNum = nums[0]

        n = len(nums)
        window_len = 0
      
        # while right < n:
        
        for right in range(n):

            minNum = min(minNum, nums[right])
            maxNum = max(maxNum, nums[right])

            if maxNum - minNum > 2:
                window_len = right - left
                count += window_len * (window_len + 1) // 2

                # Start new window at current position
                left = right 
                minNum = nums[right]
                maxNum = nums[right]

                while left > 0 and abs(nums[right] - nums[left - 1]) <= 2:
                    left -= 1
                    minNum = min(minNum, nums[left])
                    maxNum = max(maxNum, nums[left])
                

                # Remove overcounted subarrays if left boundary expanded
                if left < right:
                    window_len = right - left
                    count -= window_len * (window_len + 1) // 2
            
            # right+=1
         # Add subarrays from final window
        window_len = right - left + 1
        count += window_len * (window_len + 1) // 2

        return count

        
                
