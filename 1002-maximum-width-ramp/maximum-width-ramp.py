class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        # Sliding Window
        #Maximum Width Ramp - Leetcode 962 - Python
        # https://www.youtube.com/watch?v=3pTEJ1vzgSI

        n = len(nums)
        right_max = [None] * n

        # Fill right_max array with the maximum values from the right
        right_max[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i])
        
        # print(right_max)

        left = 0
        right = 0
        max_width = 0

        # Traverse the array using left and right pointers
        while right < n:
            # Move left pointer forward if current left exceeds right_max
            while nums[left] > right_max[right]:
                left += 1

            if left < right:
                max_width = max(max_width, right - left)
            right += 1

        return max_width
        
        