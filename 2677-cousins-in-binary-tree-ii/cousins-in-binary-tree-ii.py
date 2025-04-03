# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None

        queue = deque([root])
        level_arr = []
        while queue:
            size = len(queue)
            level_sum = 0
            for _ in range(size):
                node = queue.popleft()
                level_sum+= node.val

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            level_arr.append(level_sum)
        
        root.val = 0
        queue = deque([root])
        level_idx = 1

        while queue:
            size = len(queue)
            for _ in range(size):

                node = queue.popleft()

                curr_group_sum = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)

                if node.left:
                    node.left.val = level_arr[level_idx] - curr_group_sum
                    queue.append(node.left)
                
                if node.right:
                    node.right.val = level_arr[level_idx] - curr_group_sum
                    queue.append(node.right)
            level_idx+=1
        return root
                
        
