class Solution:

    # How is this Minimize the Maximum hence BS ?

    # Well we ned to return minimum integer k
    # k = # Bananas per Hour

    # This k can a number b/w 1 and  max(piles) = [1,11]: eg 1
    # it can maximum possible to finish before guard come at hour "h"

    # But Q: Asks for minimum Posible K
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)

        # BS on k
        while left < right:
            mid = (left+right) // 2
        
            if self.is_possible(mid, piles,h):
                right = mid
            else:
                left = mid + 1

        return left
    
    def is_possible(self, k_candidate, piles, h):
        # total_hours = 0
        hour_spent = 0

        for pile in piles:
            hour_spent += math.ceil(pile / k_candidate)
            # total_hours += pile_hr
        return hour_spent<=h


#Time complexity: O(n⋅logm)
#Let n be the length of the input array piles and m be the maximum number of bananas in a single pile from piles.


