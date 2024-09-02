# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        # if not root:
        #     return root

        # q = deque()
        # q.append(root)

        # while q:
        #     curr = q.popleft()

        #     curr.left, curr.right = curr.right, curr.left
        #     if curr.left!=None:
        #         q.append(curr.left)


        #     if curr.right!=None:
        #         q.append(curr.right)
        
        
        # return root
        
        # Recursive

        if not root:
            return root
        
        # Step 1
        root.left, root.right = root.right, root.left
        # Step 2
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

        # We can reverse Step 1 and Step 2 order
        # One will be top down, other will be bottom up
        # Top Down: VLR 
        # Bottom Up: LRV
        