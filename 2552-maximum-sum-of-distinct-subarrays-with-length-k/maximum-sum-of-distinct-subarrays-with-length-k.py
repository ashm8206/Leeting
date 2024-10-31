class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        l = 0 
        n = len(nums)
        hmap = defaultdict(int)

        curr_sum = 0
        maxSum = 0

        for r in range(n):
         
            hmap[nums[r]] += 1
            curr_sum+= nums[r]
        
            if r-l+1 > k:
                curr_sum-=nums[l]
                hmap[nums[l]]-=1
                if hmap[nums[l]]==0:
                    del hmap[nums[l]]
                l+=1
                
            if len(hmap)==k:
                maxSum = max(maxSum, curr_sum)

        return maxSum
            

        
