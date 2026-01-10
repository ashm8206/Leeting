from collections import defaultdict
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        l = 0 
        n  = len(nums)
        hmap = defaultdict(int)
        maxScore = 0
        score = 0

        for r in range(n):
            score += nums[r]
            hmap[nums[r]]+=1

            while hmap[nums[r]] > 1:
                # shrink
                hmap[nums[l]] -= 1
                score -= nums[l]
                l+=1
            
            maxScore = max(maxScore, score)
            
        return maxScore


        