# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        if not root:
            return []

        q = deque()
        q.append((root,0))

        level = 0
        res = []
       
        while q:
            level_len = len(q)
            res.append([])
            

            for i in range(level_len):

                curr, curr_level = q.popleft()
                res[level].append(curr.val)

                if curr.left:
                    q.append((curr.left,curr_level+1))
                
                if curr.right:
                    q.append((curr.right,curr_level+1))

            level+=1
            
        return res
