class Solution:
    def canJump(self, nums: List[int]) -> bool:

        dis = 0
        n = len(nums)

        for i in range(0, n):
            dis = max(dis, i+nums[i])
            if dis >= n-1:
                return True

            if dis<=i:
                return False
                
        return True