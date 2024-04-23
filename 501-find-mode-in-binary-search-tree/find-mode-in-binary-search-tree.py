# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        # inorde on BST will be sorted
        res = []
        def inOrder(root):
            if not root:
                return 

            inOrder(root.left)
            res.append(root.val)
            inOrder(root.right)
        
        inOrder(root)

        current_streak = 0
        max_streak = 0
        num = 0

        for curr_num in res:
            if num==curr_num:
                current_streak+=1
                
            else:
                current_streak = 1
                num = curr_num
            
            if current_streak > max_streak:
                ans = []
                max_streak = current_streak

            if current_streak == max_streak:
                ans.append(num)

        return ans
