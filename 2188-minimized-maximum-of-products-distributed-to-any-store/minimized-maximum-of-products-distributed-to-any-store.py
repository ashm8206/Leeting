class Solution:
    def minimizedMaximum(self, n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """

        left = 0
        right = max(quantities)

        # Perform binary search until the boundaries converge
        while left < right:
            middle = (left + right) // 2
            if self.can_distribute(middle, quantities, n):
                # Try for a smaller maximum
                right = middle
            else:
                # Increase the minimum possible maximum
                left = middle + 1

        return left
    
    def can_distribute(self, x: int, quantities: List[int], n: int) -> bool:

        j = 0 
        # pointer to the first not fully distributed product
        remaining = quantities[j]
        

        for i in range(n):

            if remaining <=x:
                # this less than x quantity will be taken by a store
                j+=1
                if j==len(quantities):
                    return True
                else:
                    remaining = quantities[j]
            else:
                remaining-=x
        return j==len(quantities)


        
        