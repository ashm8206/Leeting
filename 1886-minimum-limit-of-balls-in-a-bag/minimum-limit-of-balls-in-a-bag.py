class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
     

        # Binary search bounds
        # left binary search
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
           
                number_of_bags = math.ceil(num / max_balls_in_bag)
                operations = number_of_bags - 1
                total_operations += operations

            return total_operations <= max_operations