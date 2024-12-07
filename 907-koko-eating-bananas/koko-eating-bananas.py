class Solution:
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
            hour_spent += math.ceil(pile/k_candidate)
            # total_hours += pile_hr
        
        if hour_spent <= h:
            return True
        return False
