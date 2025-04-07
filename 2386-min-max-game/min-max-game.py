class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        
        n = len(nums)
        while n  > 1:

            result = [0]* (n//2)
            for i in range(len(result)):
                if i%2:
                    result[i] = max(nums[2 * i], nums[2 * i + 1])
                else:
                    result[i] = min(nums[2 * i], nums[2 * i + 1])
            nums = result
            n = len(nums)
        return nums[0]