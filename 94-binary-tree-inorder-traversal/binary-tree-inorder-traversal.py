# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        # while curr is not None or len(stack) > 0 :
        #     #Keep going Left L
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
        #     # can't go Left anymore LV
        #     curr = stack.pop()
        #     res.append(curr.val)
        #     # Go Right LVR
        #     curr = curr.right
        # return res

        if not root:
            return res

        curr = root
        stack = []
        
        while stack or curr is not None: # OR

            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop() # Pop Leftmost
            res.append(curr.val) # Add Value

            curr = curr.right # Go Right
        
        
        return res
        

            