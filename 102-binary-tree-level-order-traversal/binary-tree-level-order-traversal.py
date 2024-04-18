# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        if not root:
            return []

        q = deque()
        q.append((root,0))

        level = 0
       
        while q:
            level_len = len(q)
            level_ls = []
            

            for i in range(level_len):

                curr, curr_level = q.popleft()

                if curr.left:
                    q.append((curr.left,curr_level+1))
                
                if curr.right:
                    q.append((curr.right,curr_level+1))

                level_ls.append(curr.val)
                
            res.append(level_ls)
            level+=1
            
        return res
