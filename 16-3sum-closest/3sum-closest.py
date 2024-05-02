class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort() # --> Nlogn, O(n) with Counting Sort
        result = 0
        minDist = 10**9
        n = len(nums)
        for i in range(n):
            # if i > 0 and nums[i-1]==nums[i]:
            #     continue

            left = i+1
            right = n-1
            while left < right:
        
                currSum = nums[i]+ nums[left]+nums[right]
                if abs(currSum - target) <= minDist:
                    minDist = abs(currSum - target)
                    result = currSum
                if  currSum > target:
                    right-=1
                else:
                    left+=1
                
            
        return result
        #-4,-1,1,2
        # -3 <= k  -3-1 == -4
        #-4+1+2 = -1-1 = -2
