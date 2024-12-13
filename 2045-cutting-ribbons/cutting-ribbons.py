class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        # Determine Max Length X
        # When take  Num_cuts >=k or number<k

        # # [3,4,5,9]
        #    T T T F

        def isPossible(ans, ribbons, k):
            count_cuts = 0
            for val in ribbons:
                count_cuts += val // ans
            print(count_cuts >=k)
            return count_cuts >=k

        # ribbons.sort()

        left = 0
        right = max(ribbons)

        while left < right:
            mid = (left + right + 1) // 2

            if isPossible(mid, ribbons, k):
                left = mid
            else:
                right = mid - 1
        return left


        