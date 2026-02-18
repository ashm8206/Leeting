class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        if k == 1:
            return nums  # If k is 1, every single element is a valid subarray

        n = len(nums)
        result = [-1] * (n - k + 1)
        consecutive_count = 1  # Count of consecutive elements

        for i in range(n-1):
            if nums[i] + 1 == nums[i + 1]:
                consecutive_count += 1
            else:
                consecutive_count = 1  # Reset count if not consecutive

            # If we have enough consecutive elements, update the result
            if consecutive_count >= k:
                result[i+1-k+1] = nums[i+1]

        return result        
    
        return res

    