# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        queue = collections.deque()
        queue.append((root,0))

        while queue:
            level_len = len(queue)
            
            prev = None
            for i in range(level_len):
                node, level = queue.popleft()
                
                if level%2==1:
                    if prev and prev <= node.val or node.val % 2 == 1:
                        return False
                else:
                    if prev  and prev >= node.val or node.val % 2 == 0:
                        return False
                
                prev = node.val

                if node.left:
                    queue.append((node.left, level+1))
                
                if node.right:
                    queue.append((node.right,level + 1))
        return True
                
                


