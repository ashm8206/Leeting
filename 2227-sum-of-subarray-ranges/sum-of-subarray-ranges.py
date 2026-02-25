import operator
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        

        def monotono_stack(op = operator.ge):
            stack = []
            ans = 0
            for i in range(len(nums)+1):

                while stack and (i ==len(nums) or op(nums[stack[-1]], nums[i])):

                    # Notice the sign ">=", This ensures that no contribution
                    # is counted twice. right_boundary takes equal or smaller 
                    # elements into account while left_boundary takes only the
                    # strictly smaller elements into account

                    mid = stack.pop()
                    # for mid, nextSmaller is at i
                    # previousSamller is at stack[-1]

                    right_boundary = i 
                    left_boundary = -1 if not stack else stack[-1]
                    

                    # count of subarrays where mid is the minimum element
                    # Don't count the left or right boundary element
                    # Product so pairs and Not counts
                    pair_count = (mid - left_boundary) * (right_boundary - mid)
                    ans += (pair_count * nums[mid])

                stack.append(i)
            return ans
        sum_of_minimums = monotono_stack(operator.ge)
        sum_of_maximums = monotono_stack(operator.le)
        return sum_of_maximums - sum_of_minimums

