class Solution:
    def mySqrt(self, x: int) -> int:

        # Method 1
        # left, right = 0, x + 1
        # while left < right: # space has to be atleast 2
            
        #     mid = left + (right - left) // 2
        #     # print(left, right, mid)
        #     if mid * mid > x:
        #         right = mid # to manintain the lemma that right + 1 than x
        #     else:
                
        #         left = mid + 1
        #     # print(left, right, mid)
        # return left - 1 #Right == Left but as we set right + 1 than x for edge case and in lemma, when Right==Left it breaks out.  As right + 1 than the answer, we subract -1 before reporting


        # Method II

            # Base cases
        if (x == 0 or x == 1):
            return x

        # Do Binary Search for floor(sqrt(x))
        start = 1
        end = x//2
        while (start <= end):
            mid = (start + end) // 2

            # If x is a perfect square
            if (mid*mid == x):
                return mid

            # Since we need floor, we update
            # answer when mid*mid is smaller
            # than x, and move closer to sqrt(x)
            if (mid * mid < x):
                start = mid + 1
                ans = mid

            else:

                # If mid*mid is greater than x
                end = mid-1
        return ans