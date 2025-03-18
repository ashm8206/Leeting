class Solution:
    def minimizedMaximum(self, n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """

        left = 1
        right = max(quantities)

        # Left Most Binary Search
        while left < right:
            mid = (left + right) // 2
            if self.can_distribute(mid, quantities, n):
                # Try for a smaller maximum
                right = mid
            else:
                # Increase the minimum possible maximum
                left = mid + 1

        return left
    
    def can_distribute(self, x: int, quantities: List[int], n: int) -> bool:

       

        # Method I
        total_stores = 0
        for qty in quantities:
            total_stores += math.ceil(qty/x)
        
        return total_stores<=n

        # j = 0 
        # pointer to the first not fully distributed product
        # remaining = quantities[j]
        

        # for i in range(n):

        #     if remaining <=x:
        #         # this less than x quantity will be taken by a store
        #         j+=1
        #         if j==len(quantities):
        #             return True
        #         else:
        #             remaining = quantities[j]
        #     else:
        #         remaining-=x
        # return j==len(quantities)







        
        