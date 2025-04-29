# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def preorder(r: TreeNode, curr_number: int) -> None:
            nonlocal root_to_leaf
            if r:
                curr_number = curr_number * 10 + r.val
                # if it's a leaf, update root-to-leaf sum
                if not (r.left or r.right):
                    root_to_leaf += curr_number

                preorder(r.left, curr_number)
                preorder(r.right, curr_number)

        root_to_leaf = 0
        preorder(root, 0)
        return root_to_leaf
        # if not root:
        #     return 0

        # res = []
        # def helper(root, path):
        #     if not root:
        #         return 

        #     path.append(str(root.val))
        #     if root.left is None and root.right is None:
        #         res.append(int("".join(path[:])))
        #         return 

        #     if root.left:
        #         helper(root.left,path)
        #         path.pop()

        #     if root.right:
        #         helper(root.right,path)
        #         path.pop()
        
        # helper(root, [])
        # return sum(res)
  
            
            