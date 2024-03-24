# Definition for a binary tree node.
from collections import deque
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        # if len(root)==1:
        #     return res[root.val] # ?

        queue = deque()

        queue.append((root))

        flip_bit = 0

        while queue:
            len_of_level = len(queue)
            curr_level = []
            for _ in range(len_of_level):
                node = queue.popleft()
                # Append values to res for curr level
                curr_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # now queue has all elements of next level
            if flip_bit:
                curr_level = curr_level[::-1]
            flip_bit^=1
            res.append(curr_level)
        return res
                
                



        