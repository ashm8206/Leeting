from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        # minNum = nums[0]
        # maxNum = nums[0]

        # n = len(nums)
        # left = 0
        # right = 0

        # ans = -1
        # for right in range(n):

        #     minNum = min(minNum, nums[right])
        #     maxNum = max(maxNum, nums[right])

        #     if abs(maxNum - minNum) > limit :
        
        #         left = right
        #         minNum = nums[right]
        #         maxNum = nums[right]

        #         while left > 0  and abs(nums[right] - nums[left-1]) <= limit:
        #             left-=1
        #             minNum = min(minNum, nums[left])
        #             maxNum = max(maxNum, nums[left])
            
        #     ans = max(ans, right - left + 1)

        # return ans

        '''
        two pointer technique, we need to make it as long as possible need to keep expanding
        need fast way to find min and maximum between some interval (i,j) inclusive
        then we can use two poiniter effeciently
        need to use Sorted List to represent the subarray, then we can check
        use .remove
        '''
        sl = SortedList([])
        ans = -1
        left = 0
        N = len(nums)
        for right in range(N):
            sl.add(nums[right])
            while left < right and sl[-1] - sl[0] > limit:
                sl.remove(nums[left])
                left += 1
            
            if sl[-1] - sl[0] <= limit:
                ans = max(ans,len(sl))
        
        return ans


        