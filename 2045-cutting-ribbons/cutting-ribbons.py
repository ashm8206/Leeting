class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        # Determine Max Length X
        # When take  Num_cuts >=k or number<k

        # # [3,4,5,9]
        #    T T T F

        def isPossible(cand, ribbons, k):
            count_cuts = 0
            for val in ribbons:
              
                count_cuts += math.ceil(val // cand)
                # You can discard any leftover ribbon from the cuts.
                # hence floor
            
            return count_cuts >=k

    
        # rightmost Binary search

        left = 0 # or perform NO cuts at all
        right = max(ribbons)

        while left < right:
            mid = (left + right + 1) // 2
            # left = mid --> infinite loop
            # add 1

            if isPossible(mid, ribbons, k):
                left = mid
            else:
                right = mid - 1
        return left


        