class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num = 1
        n = len(arr)
        l = 0
        r = n

        # l, r = 0, len(nums) # --> leftmost binary search
        # # regular if found, elif and else --> l -> 0 , r = n-1

        # https://leetcode.com/problems/kth-missing-positive-number/solutions/1004535/python-two-solutions-o-n-and-o-log-n-explained/
        while l < r:
            mid = (l+r)//2

            #    arr = [2, 3, 4, 7, 11, 12]
            # # Missing = [1, 1, 1, 3, 6, 6] ?
            # Missing = 11 - [4+1] = 6

            # a[i]- [ith Index + 1]
            if arr[mid] - (mid +1) < k:
                l = mid + 1
            else:
                r = mid
        #found the pt where there are k missing numbers
        #Jumping k steps to the missing number: return ans

        return l + k
