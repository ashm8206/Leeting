# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # self.ans = 0
        # def helper(root):
        #     nonlocal k
        #     if not root:
        #         return None
        #     left = helper(root.left)
        #     if left is not None:
        #         return left
        #     k-=1
        #     if k==0:
        #         # self.ans = root.val
        #         return root.val
        #     return helper(root.right)
        
        # # helper(root)
        # # return self.ans
        # return helper(root)
        

        curr = root
        stack = []

        while stack  or curr:

            while curr:
                # if you no longer can go left
                # you are at the left most node / at the parent VR
                # where more nodes in the right subtree

                # keep a track of what you saw in the stack
                # You may need to pop it later
                stack.append(curr)
                # keep track of it before you curr = curr.left

                curr = curr.left

            curr = stack.pop()
            k-=1
            if k==0:
                return curr.val
            curr = curr.right # lefmost node
        


        
        


