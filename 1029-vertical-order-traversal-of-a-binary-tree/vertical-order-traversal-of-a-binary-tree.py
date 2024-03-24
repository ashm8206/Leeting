from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        column_map = defaultdict(list)

        min_col = 10**5

        max_col = -10**5

        if root is None:
            return []

        queue = deque()
        queue.append((root, 0,0))

        while queue:
            len_of_queue = len(queue)

            for _ in range(len_of_queue):

                node, row, col_idx = queue.popleft()

                if node.left:
                    queue.append((node.left, row+1, col_idx-1))

                if node.right:
                    queue.append((node.right, row+1, col_idx+1))
                
                min_col = min(min_col, col_idx)
                max_col = max(max_col, col_idx)

                column_map[col_idx].append((row, node.val))
        res = []
        for col in range(min_col, max_col+ 1):
            # sort first by 'row', then by 'value', in ascending order
            res.append([val for row, val in sorted(column_map[col])])
        return res
        #return [sorted(column_map[col_idx], key = lambda x: x[0]) for col_idx in range(min_col, max_col+1)]
