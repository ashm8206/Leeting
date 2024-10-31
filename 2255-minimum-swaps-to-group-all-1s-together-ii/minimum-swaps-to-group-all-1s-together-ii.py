class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = sum(nums)
        cnt_one = max_one = 0
        left = right = 0
        n = len(nums)
        # Fixed Window
        for right in range(2*n):
            # updating the number of 1's by adding the new element
            cnt_one += nums[right%n]
           
            # maintain the length of the window to ones
            if right - left + 1 > ones:
                # updating the number of 1's by removing the oldest element
                cnt_one -= nums[left%n]
                left += 1
            # record the maximum number of 1's in the window
            max_one = max(max_one, cnt_one)
        return ones - max_one