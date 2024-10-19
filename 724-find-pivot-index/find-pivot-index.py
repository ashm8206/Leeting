class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        n = len(nums)

        # if n == 1:
        #     return 0

        left = 0
        total = sum(nums)
        right = total

        for i in range(0, n):

            right -= nums[i]

            if i == 0 and right==0:
                return 0
            elif i==n-1 and left==0:
                return n-1
            else:
        
                if left == right:
                    return i
            left+= nums[i]
        return -1

        # if i > 0, left = 0
        # 2-2 = 0 left =0
        