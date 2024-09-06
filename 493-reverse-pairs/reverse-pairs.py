class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        elems = []
        N = len(nums)
        ans = 0
        for ii in range(N-1, -1, -1):
            at = bisect_left(elems, nums[ii])
            if at:
                ans += at
            insort(elems, nums[ii] * 2)
        return ans
        # worst case, which is O(n log n). 
        # The algorithm as a whole still has a running time of O(n2) on average because of the series of swaps required for each insertion.
        return counts
        # https://leetcode.com/problems/reverse-pairs/solutions/355494/simple-python-bisect-solution/