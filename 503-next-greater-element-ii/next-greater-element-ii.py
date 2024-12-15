class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # https://www.youtube.com/watch?v=WLrA8X66mQs

        n = len(nums)
        nextGreater = [-1]*n
        stack = []


        for i in range(2*n):
            while stack and nums[stack[-1]] < nums[i%n]:
                stackTopIdx = stack.pop()
                nextGreater[stackTopIdx] = nums[i%n]
            # print(i, nextGreater, stack)
            stack.append(i%n)
        return nextGreater
