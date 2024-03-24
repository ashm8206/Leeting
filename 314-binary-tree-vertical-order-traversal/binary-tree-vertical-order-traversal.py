from collections import deque, defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 9, 3, 15 20 7
        column_map = defaultdict(list)

        min_col = 10**5

        max_col = -10**5

        if root is None:
            return []

        queue = deque()
        queue.append((root, 0))

        while queue:
            len_of_queue = len(queue)

            for _ in range(len_of_queue):

                node, col_idx = queue.popleft()

                if node.left:
                    queue.append((node.left, col_idx-1))

                if node.right:
                    queue.append((node.right, col_idx+1))
                
                min_col = min(min_col, col_idx)
                max_col = max(max_col, col_idx)

                column_map[col_idx].append(node.val)

        return [column_map[x] for x in range(min_col, max_col+1)]

                


        

    