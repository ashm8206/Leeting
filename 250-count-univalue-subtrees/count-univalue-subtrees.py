# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:

        count = 0

        def helper(node):
            nonlocal count

            if node is None:
                return True
            
            
            l_unival = helper(node.left)
            r_unival = helper(node.right)

            if l_unival  and r_unival:

                if node.left and node.left.val!=node.val:
                    return False
                
                if node.right and node.right.val!=node.val:
                    return False
                
                # node.left is None and/or Right is None
                # exists and node.left == node.right
                count+=1 
                return True
            else:
                # cant be unival subtree
                return False
      
          
        helper(root)
        return count


            #  1 single child
            #  2 children
        # count = 0

        # def helper(root):
        #     nonlocal count

        #     if not root:
        #         return True
            
        #     l_unival = helper(root.left)
        #     r_unival = helper(root.right)

        #     if l_unival and r_unival:
        #         # check if parent ==lc and parent==rc 
        #         # or rc is none or lc id none
        #         if root.left and root.left.val != root.val:
        #             return False
        #         if root.right and root.right.val != root.val:
        #             return False
                
        #         count+=1
        #         return True
        #     else:
        #         # cant be unival subtree
        #         return False
        # helper(root)
        # return count
                

            