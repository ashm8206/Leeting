class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # https://www.youtube.com/watch?v=WLrA8X66mQs

        n = len(nums)
        nextGreater = [-1]*n
        stack = []

        # loop twice
        # Basically, the 2nd loop is for the Last element / elements in stack
        # idx, will be added to the stack, 
            # we do a nother loop to catch any element greater than curr
        for i in range(2*n):
            while stack and nums[stack[-1]] < nums[i%n]:
                stackTopIdx = stack.pop()
                nextGreater[stackTopIdx] = nums[i%n]
            stack.append(i%n)
        return nextGreater
