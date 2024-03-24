from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #  bfs, level(?)
    #  2^0, = 1
    #  2^1 = 2
    #  2^2 = 4
    #  2^3 = 8   
    #  max(maxWidth, min(2^level, ))
    #  Parent node PL--> Leaf node Left substree, H+1
    #  Parent node --> Leaf node Right substree, H+1
    #  if H_L!=H_R:
    #    min(H_L,H_R) --> 2^H
    #  else:
        # if PL.L not set:  2^H - 1
        # if P.R not set:   2^H - 1  
        
        if not root:
            return 0
        
        max_width = -1
        
        queue = deque()
        queue.append((root,0)) # node, and col_index
        
        while queue:
            level_length = len(queue)

            _, start_idx = queue[0]
            _, end_idx = queue[-1]
            
            for idx in range(level_length):
                node, col_idx = queue.popleft()
            
                if node.left:
                    queue.append((node.left, col_idx*2))
                    
                if node.right:
                    queue.append((node.right, col_idx*2+1))
                    
            # It is not the number of Nodes        
            # max_width = max(max_width, level_length)
            
            # It is the indexes after accounting for Null's in between            
            max_width = max(max_width,  end_idx - start_idx + 1)
            # print(start_idx, end_idx+1)
            
        return max_width
        
        