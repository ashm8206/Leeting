class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
    # def twoSum(self, nums,firstIdx = 1, left=None,right=None,target=None):

    #     tempRes = []
    #     while left < right:
            
    #         if left-1 > firstIdx and nums[left]==nums[left-1]:
    #             # print(left, firstIdx, right)
    #             left+=1
    #             continue
    #         if (nums[left] + nums[right]) <= target: 
    #             if nums[left] + nums[right] == target:
    #                 tempRes.append([-target, nums[left],nums[right]])

    #             left+=1
    #         elif (nums[left] + nums[right]) > target :
    #             right-=1

    #     return tempRes

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     res = []
    #     n = len(nums)
    #     nums.sort()
    #     for i in range(0, n-2):
    #         if i > 0 and nums[i] == nums[i-1]:
    #             continue
    #         temp = self.twoSum(nums, firstIdx = i ,left=i+1, right=n-1, target = -nums[i])
    #         # print(temp, i)
    #         if temp:
    #             res.extend(temp)
    #     return res

# TestCase: [0,0,0,0]