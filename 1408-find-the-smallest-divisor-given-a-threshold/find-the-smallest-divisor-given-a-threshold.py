class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def condition(divisor) -> bool:
            sums = 0
            for num in nums:
                sums+=  math.ceil(int(num)/ mid)
            return sums <=threshold

        left, right = 1, max(nums)
        while left < right:
            mid = left + (right - left) // 2

            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left