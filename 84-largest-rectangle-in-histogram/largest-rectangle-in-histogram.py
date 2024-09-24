class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        max_area = -2**31
        n = len(heights)
        # stack = []
        

        # for curr_idx, h in enumerate(heights):
            
        #     start_idx = curr_idx

        #     while stack and stack[-1][1] > h:
        #         old_idx, old_height = stack.pop()
        #         max_area = max(max_area, old_height * (curr_idx - old_idx))
        #         start_idx = old_idx 
                
        #         # where the previous one ended becomes start indx of the smaller building/historgram
        #     stack.append((start_idx,h))
        
        # if stack: # we extend it ahead.
        #     for  curr_idx, h in stack:
        #         max_area = max(max_area, h * (n - curr_idx))
        # return max_area

        stack = [(-1,0)]

        for right_idx , h in enumerate(heights):

            while stack[-1][0]!=-1 and stack[-1][1] > h:
                _ , curr_height = stack.pop()
                curr_width = right_idx - stack[-1][0] - 1
                max_area = max(max_area, curr_height*curr_width)
            stack.append((right_idx, h))
        
        while stack[-1][0]!=-1:
            _ , curr_height = stack.pop()
            curr_width = n - stack[-1][0] - 1
            max_area = max(max_area, curr_height*curr_width)
        return max_area