# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # if not preorder and not inorder:
        #     return None

        hmap = {val: i for i, val in enumerate(inorder)}
        def helper(preorder, inorder):
            if not inorder:
                return None

            val = preorder.pop(0)
            root = TreeNode(val)
            mid = hmap.get(val)
            
            root.left = self.buildTree(preorder, inorder[:mid])
            root.right = self.buildTree(preorder, inorder[mid+1:])

            # root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
            # root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
            # print(preorder[1:mid+1], mid, preorder[mid+1:])
            return root
        return helper(preorder, inorder)
        