from collections import deque, defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        colMap = defaultdict(list)
        if not root:
            return[]

        q = deque()
        q.append((root,0)) #01st col
        maxCol = -2**31 - 1
        minCol = 2**31 + 1

        while q:
            node, col = q.popleft()

            if node.left:
                q.append((node.left, col-1))
            
            if node.right:
                q.append((node.right, col+1))
            
            colMap[col].append(node.val)
            

            maxCol = max(maxCol, col)
            minCol = min(minCol, col)

        res = []
        for cIdx in range(minCol, maxCol+1):
            res.append(colMap[cIdx])
        
        return res
            






        # # 9, 3, 15 20 7
        # column_map = defaultdict(list)

        # min_col = 10**5

        # max_col = -10**5

        # if root is None:
        #     return []

        # queue = deque()
        # queue.append((root, 0))

        # while queue:
        #     len_of_queue = len(queue)

        #     for _ in range(len_of_queue):

        #         node, col_idx = queue.popleft()

        #         if node.left:
        #             queue.append((node.left, col_idx-1))

        #         if node.right:
        #             queue.append((node.right, col_idx+1))
                
        #         min_col = min(min_col, col_idx)
        #         max_col = max(max_col, col_idx)

        #         column_map[col_idx].append(node.val)

        # return [column_map[x] for x in range(min_col, max_col+1)]

                


        

    