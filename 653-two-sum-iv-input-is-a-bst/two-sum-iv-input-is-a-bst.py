# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        path = []

        # Inorder on BST is sorted

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            path.append(root.val)
            inorder(root.right)
        
        inorder(root)
        
        l = 0
        r = len(path) - 1

        while l < r:
            if path[l] + path[r] == k:
                return True
            elif path[l] + path[r] > k:
                r -=1
            else:
                l+=1

        return False
