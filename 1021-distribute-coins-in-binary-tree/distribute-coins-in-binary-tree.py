# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:

        moves = 0

        def helper(root):
            nonlocal moves
            if root is None:
                return 0
            
            leftMoves = helper(root.left)
            rightMoves = helper(root.right)

            moves += abs(leftMoves) + abs(rightMoves)
            # Gain or Losing  is the same as 1 move
            
            return root.val + leftMoves + rightMoves - 1

            #     0  1       2+ 1
            #  0  (1, 1)    2
            # 2, 2

            #    4.     (-3) ==> abs 
            #  0    0  (-2, , -1)
            # 0        (-1)
        helper(root)

        return moves