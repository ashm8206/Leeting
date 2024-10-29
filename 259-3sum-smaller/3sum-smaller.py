class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        n = len(nums)
        for i in range(n-2):
            res += self.twoSumSmaller(nums, i + 1, n-1, target - nums[i])
        
        return res

    def twoSumSmaller(self, nums, left, right, target):

        res = 0
        while (left < right):

            if (nums[left] + nums[right] < target):
                res += right - left  # use left as the pivot, every number i+1 + j forms a pair
                
                left+=1
            else:
                right-=1
        
        return res