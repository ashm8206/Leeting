class Solution:
    def twoSum(self, nums,firstIdx = 1, left=None,right=None,target=None):

        tempRes = []
        while left < right:
            
            if left-1 > firstIdx and nums[left]==nums[left-1]:
                # print(left, firstIdx, right)
                left+=1
                continue
            if (nums[left] + nums[right]) <= target: 
                if nums[left] + nums[right] == target:
                    tempRes.append([-target, nums[left],nums[right]])

                left+=1
            elif (nums[left] + nums[right]) > target :
                right-=1

        return tempRes

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        for i in range(0, n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            temp = self.twoSum(nums, firstIdx = i ,left=i+1, right=n-1, target = -nums[i])
            # print(temp, i)
            if temp:
                res.extend(temp)
        return res

    # def twoSum(self, start,end,idx,nums):
    #     key = -nums[idx]
    #     i = start
    #     j = end

    #     n = len(nums)
    #     res = set()
    #     while i < j:
    #         if (nums[i] + nums[j]) < key :
    #             i+=1
    #         elif (nums[i] + nums[j]) > key:
    #             j-=1
    #         else:
    #             res.add((nums[idx],nums[i],nums[j]))
    #             i+=1
    #             j-=1
    #             while i < j and nums[i] == nums[i - 1]:
    #                 i += 1
    #     return res

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res= []
        # nums.sort()
        # # print(nums)
        # n = len(nums)
        # for i in range(n):
        #     if i > 0 and nums[i-1]==nums[i]:
        #         continue

        #     result = self.twoSum(i+1,n-1,i,nums)
        #     # why do we pass i+1,
        #     # cuz it is assumed that for i-1, nums 
        #     # Triplets that statisfy the condition have already been found.

        #     if result:
        #         res.extend(list(result))
        # return res

#    
