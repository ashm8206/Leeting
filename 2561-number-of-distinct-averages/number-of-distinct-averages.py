class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        res = set()

        nums.sort() #---> Reduced to O(n) for counting sort

        def cSort(nums):

            n = len(nums)
            maxNum = 100
            output = [0]*n
            counts = [0]*(maxNum+1)

            for num in nums:
                counts[num]+=1
            
            for i in range(maxNum+1):
                if i > 0:
                    counts[i]+=counts[i-1]

            for num in nums:
                output[counts[num]-1]=num
                counts[num]-=1
            
            return output
        
        nums = cSort(nums)
        
        i = 0
        j = len(nums)-1
        while i < j:
            res.add((nums[i]+nums[j])/2)
            i+=1
            j-=1
        return len(res)