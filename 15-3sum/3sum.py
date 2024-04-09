class Solution:

    def twoSum(self, start,end,idx,nums):
        key = -nums[idx]
        i = start
        j = end
        res = set()
        while i < j:
            if (nums[i] + nums[j]) < key:
                i+=1
            elif (nums[i] + nums[j]) > key:
                j-=1
            else:
                res.add((nums[idx],nums[i],nums[j]))
                j-=1
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res= []
        nums.sort()
        print(nums)
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i-1]==nums[i]:
                continue

            result = self.twoSum(i+1,n-1,i,nums)

            if result:
                res.extend(list(result))
        return res

       




        