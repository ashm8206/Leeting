# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q =  collections.deque([(root, 0)])

        while q:
            level_len = len(q)
            res = set()
            for _ in range(level_len):
                node, parent = q.popleft()
                if node.val in {x, y} and parent not in res:
                    res.add(parent)
                if len(res)==2:
                    return True
                if node.left:
                    q.append((node.left, node.val))
                if node.right:
                    q.append((node.right, node.val))
        return False

        # 1,0
        # res = {}
        # for _ in node(level_len):
        #   curr, parent = popleft 
        #   if curr in set{x,y} and parent not in res:
        #        res.append(parent)
        #  
        #  if len(res)==2:
        #       return True
        #   if node.left, if node.right
        #      q.(node.val, parent)
        # return False Outside Q

        