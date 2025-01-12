# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.ans = 0
        def helper(root):
            nonlocal k
            if not root:
                return None
            helper(root.left)
            k-=1
            if k==0:
                self.ans = root.val
            helper(root.right)
        
        helper(root)
        return self.ans
        

        
        # if not root:
        #     return -1

        # curr = root
        # stack = [curr]

        # while True:

        #     if curr:
        #         stack.append(curr)
        #         curr = curr.left
            
        #     elif stack:
        #         curr = stack.pop()
        #         k-=1 
        #         if k==0:
        #             return curr.val
                
            
        #         curr = curr.right
        #     else:
        #         break


        
        


