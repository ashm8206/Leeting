class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)

        # calculate difference array 
        # includes +ve and -ve values
        diff = [target[i] - nums[i] for i in range(n)]

        min_ops = abs(diff[0])

        for i in range(1, n):
            # if both differences are negative,
            if (diff[i-1] <= 0 and diff[i] <= 0) or (diff[i-1] >= 0 and diff[i] >= 0) :
                # the subsequent difference will only add operations if it is
                # more negative than the previous difference
                min_ops += max(abs(diff[i]) - abs(diff[i - 1]), 0)
            else:
                # 1 pos, 1 neg
                min_ops += abs(diff[i])
        
        return min_ops
