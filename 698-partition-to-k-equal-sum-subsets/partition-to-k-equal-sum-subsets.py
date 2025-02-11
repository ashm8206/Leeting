class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        subsetSum, remain = divmod(sum(nums), k)
        if max(nums) > subsetSum or remain > 0: 
            return False  # Prune since we can't divide `nums` into subsets where each sums is equal to `subsetSum`
        n = len(nums)

        @lru_cache(None)
        def dp(mask):
            if mask == 0: return 0
            for i in range(n):
                if (mask >> i) & 1:
                    newMask = mask ^ (1 << i)
                    remain = dp(newMask)
                    if remain == -1: continue  # Skip case can't divide by using `newMask`
                    if remain + nums[i] <= subsetSum:
                        return (remain + nums[i]) % subsetSum
            return -1

        return dp((1 << n) - 1) == 0
        
        nums_sum = sum(nums)
        if nums_sum % k != 0:
            return False
        subset_sum = nums_sum / k

        ks = [0] * k
        nums.sort(reverse=True)


        def can_partition(j):
            if j == len(nums):
                for i in range(k):
                    if ks[i] != subset_sum:
                        return False
                return True

            for i in range(k):
               
                if ks[i] + nums[j] <= subset_sum:
                    ks[i] += nums[j]
                    if can_partition(j + 1):
                        return True
                    ks[i] -= nums[j]
            return False
        return can_partition(0)