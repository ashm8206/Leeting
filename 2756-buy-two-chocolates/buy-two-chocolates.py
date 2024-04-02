class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()

        left_over = money
        count = 0
        for p in prices:
            
            if left_over - p >=0:
                count+=1
                left_over -= p
                if count == 2:
                    return left_over
        return money
        
