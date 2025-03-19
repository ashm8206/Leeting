# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        q = deque()
        q.append(root)
        nullNodeFound = False

        while q:
            node = q.popleft()
            if node is None:
                nullNodeFound = True
            else:
                # if node and Nullfound is true
                # Null was found higher up/ before curr node. 
                if nullNodeFound:
                    return False
                q.append(node.left)
                q.append(node.right)
        return True