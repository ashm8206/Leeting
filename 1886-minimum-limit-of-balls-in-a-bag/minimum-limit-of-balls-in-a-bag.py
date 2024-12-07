class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # minimize maximum (or maximize minimum) => binary search
        
        # also, ceil(a / b) = (a + b - 1) // b is a useful trick.

        # Take the Biggest Numbers 1st 
        # Break them down optimal (?) 1 turn
        # [1...9]
        #  1<=  9/2, 5/2, 3/2, 2/2 : 4
        #  2<=  9/2, 5/2, 3/2  : 3
        #  3<=  9/2, 5/2 : 2
        #  4<=  9/2, 5/2 : 2


         # [8,4,2,2] : heap? : 8,4,2
        #  1<=  8/2, 4/2, 2/2 : 3(? when do you stop?)
        #  2<=  8/2, 4/2 : 2
        #  3<=  8/2, 4/2 : 2
        #  4<= 8/2 : 1 ... # Max
        #  5<= 8/2 : 1 MaxOP-1 = 3
        #----
        # 4,4,4,2
        # 1 <= 4/2 , 2/2 : 2  
        # 2 <= 4/2 : 1  # Max  smallest here(F, T,T,T) its same
        # 3<=  4/2 : 1
        #  MaxOP-1 = 2
        #---
        # 4, 4, 2,2,2,2
        # 2 <= 4/2 :1
        # MaxOP -1 = 1
        #---
        # 4,2,2,2,2, 2,2
        # 2 <= 4/2 :1 
        # MaxOP -1 = 0

        # 1. Till we have MaxOP keep doing it.
        # Start with MaxNum and break it down [1...MaxNum]
        # Based on above func. (MinSize(Bag which for which bags cant be divided further)
        #  add that to the heap.
        #
        # Once heap is over return top of heap

        # Binary search bounds
        left = 1
        right = max(nums)

        # Perform binary search to find the optimal max_balls_in_bag
        while left < right:
            middle = (left + right) // 2

            # Check if a valid distribution is possible with the current middle value
            if self._is_possible(middle, nums, maxOperations):
                # If possible, try a smaller value (shift right to middle)
                right = middle
            else:
                # If not possible, try a larger value (shift left to middle + 1)
                left = middle + 1

        # Return the smallest possible value for max_balls_in_bag
        return left
        
    def _is_possible(self, max_balls_in_bag, nums, max_operations):
            total_operations = 0

            # Iterate through each bag in the array
            for num in nums:

            #The number of bags required for bag i is:
            #   ceil(nums[i] / maxBallsInBag).

            # The number of operations for bag i is 
            # ceil(nums[i] / maxBallsInBag) - 1.
           
                operations = math.ceil(num / max_balls_in_bag) - 1
                total_operations += operations

            # If total operations exceed max_operations, return False
            if total_operations > max_operations:
                return False

            # We can split the balls within the allowed operations, return True
            return True