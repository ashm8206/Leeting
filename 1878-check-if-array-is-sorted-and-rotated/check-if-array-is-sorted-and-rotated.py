class Solution:
    def check(self, nums: List[int]) -> bool:
        
    
        n = len(nums)
        if n <= 1:
            return True

        count = 1
        for i in range(1,2*n):
            prev = (i-1)%n
            curr = i%n
            if nums[prev] <= nums[curr]:
                count+=1
            else:
                count = 1
            if count == n:
                return True
        
        return False

        # [2,1,3,4][2,1,3,4]
