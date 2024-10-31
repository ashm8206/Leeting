class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        k = 3
        cnt = 0
        n = len(nums)
        for i in range(n-k+1):
            if nums[i] == 0 :
                for j in range(3):
                    nums[i+j] = nums[i+j]^1
            
                cnt+=1
            # print(nums)
        
        return cnt if sum(nums)== len(nums) else -1