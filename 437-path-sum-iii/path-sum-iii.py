# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        # hmap = {0:1} 
        # cant have this, has to if handled with two conditions
        hmap = {0:1}
        ans = 0
        
        
        def helper(root, curr_sum):
            nonlocal ans
            if not root:
                return
            
            curr_sum += root.val
            diff = curr_sum - targetSum

            # if curr_sum == targetSum:
            #     ans+=1

            if diff in hmap:
                ans+= hmap[diff]
            

            hmap[curr_sum] = hmap.get(curr_sum, 0) + 1
            
            helper(root.left, curr_sum)
            helper(root.right, curr_sum)

            hmap[curr_sum]-=1  
            # remove the leaf node, before proceededing to parallel subtree
        helper(root, 0)
        return ans