# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        res = []
        queue = deque()
        if root:
            queue.append(root)

        while queue:
            level_list = []
            n  = len(queue)
            for _ in range(n):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_list.append(node.val)
            
            res.append(level_list)
        return res[::-1]