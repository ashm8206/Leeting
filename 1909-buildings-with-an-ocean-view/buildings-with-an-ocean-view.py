class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:


        n = len(heights)

        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()
            stack.append(i)
        return stack


        n = len(heights)
        max_so_far = heights[n-1]

        res = [n-1]

        for i in range(n-2,-1,-1):
            if heights[i] > max_so_far:
                res.append(i)
            max_so_far = max(max_so_far, heights[i])
        return res[::-1]