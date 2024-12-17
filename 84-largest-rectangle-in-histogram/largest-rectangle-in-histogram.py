class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        max_area = 0 
        n = len(heights)
        stack = []

        # Build a monotonically increasing stack
        # (Y) ht increases as X (width) increases will maximize the area.

        # if we are building a monotonically increasing array
        # we need a NextSmaller 

        """
        """
        # for the last 
        for i, h in enumerate(heights+[0]):

            while stack and heights[stack[-1]] > h:
                H = heights[stack.pop()]
                W = i if not stack else i - stack[-1]-1
                # width calculation
                # right bound where next smaller is found 
                # - left bound --> (previous smaller) 
                # - 1 (don't imclude either)
                max_area = max(max_area, H*W)
            stack.append(i)
        return max_area 

        #  1. we add h[0] to flush out the stack
        # Without that [0] to flush out the stack, we would need to basically repeat what we do in the inner while loop once at the very end of the program in case there are bars left in the stack,

        # 2. if stackEmpty W = i
        # we saw "i" larger bars before this one in the stack
        # Width = i


        # Remember width is caluclated from NextSmaller 
        # pt without account for it





        