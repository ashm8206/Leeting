class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        result = 0 
        n = len(nums)
        subsets = []

        def get_all_subset(index, nums, subset):
            if index == n:
                subsets.append(subset[:])
                return
            
            subset.append(nums[index])
            get_all_subset(index + 1, nums, subset) # Take and inc

            subset.pop() # Don't take and inc
            get_all_subset(index + 1, nums, subset)
        
        get_all_subset(0, nums, [])

        for subset in subsets:
            subset_XOR_total = 0
            for num in subset:
                subset_XOR_total ^= num
            result += subset_XOR_total
        
        return result
        