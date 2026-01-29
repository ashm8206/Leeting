class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        # subsetSum, remain = divmod(sum(nums), k)
        # if max(nums) > subsetSum or remain > 0: 
        #     return False  # Prune since we can't divide `nums` into subsets where each sums is equal to `subsetSum`
        # n = len(nums)

        # @lru_cache(None)
        # def dp(mask):
        #     if mask == 0: return 0
        #     for i in range(n):
        #         if (mask >> i) & 1:
        #             newMask = mask ^ (1 << i)
        #             remain = dp(newMask)
        #             if remain == -1: continue  # Skip case can't divide by using `newMask`
        #             if remain + nums[i] <= subsetSum:
        #                 return (remain + nums[i]) % subsetSum
        #     return -1

        # return dp((1 << n) - 1) == 0
        
        nums_sum = sum(nums)
        if nums_sum % k != 0:
            return False
        
        subset_sum = nums_sum // k
        nums.sort(reverse=True)
        #Large numbers are harder to place because they have fewer valid positions. By trying them first, you detect impossible cases sooner.
        n = len(nums)
        
        if nums[0] > subset_sum:
            return False
        
        used = [False] * n
        
        def helper(bucket_idx, current_sum, start_idx):
            # All buckets filled
            if bucket_idx == k:
                return True
            
            # Current bucket complete, start next bucket
            if current_sum == subset_sum:
                return helper(bucket_idx + 1, 0, 0)
            
            # For current bucket, decide on each element
            for i in range(start_idx, n):
                if used[i]:
                    continue
                
                # # Skip duplicates
                # if i > 0 and not used[i-1] and nums[i] == nums[i-1]:
                #     continue
                
                # Try taking this element for current bucket
                if current_sum + nums[i] <= subset_sum:
                    used[i] = True
                    
                    # "Take" this element
                    if helper(bucket_idx, current_sum + nums[i], i + 1):
                        return True
                    
                    used[i] = False
                
                # Pruning: if first element fails in empty bucket
                if current_sum == 0:
                    break
            
            # Implicitly "don't take" any element (return False)
            return False
        
        return helper(0, 0, 0)