class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        n = len(nums)
        
        if n==0:
            return [[lower,upper]]

        if lower < nums[0]:
            # print(lower, nums[0])
            res.append([lower, nums[0]-1])

        for i in range(1,n):
            if nums[i-1]+1!=nums[i]:
                res.append([nums[i-1]+1,nums[i]-1])
        
        if nums[-1]!=upper:
            res.append([nums[-1]+1,upper])
    
        return res
        


            
            

        return res

