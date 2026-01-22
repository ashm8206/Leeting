# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res = []
        path = []
        curr_sum = 0
        def helper(root, curr_sum, path):

            if not root:
                return

            path.append(root.val)
            curr_sum += root.val

            if root.left is None and root.right is None:
                if curr_sum == targetSum:
                    res.append(path[:]) # new list 
        

            #Boolean Problems vs Filling the list In Problems
            # if root.left:
            helper(root.left,curr_sum,path)
                # path.pop()
            
            # if root.right:
            helper(root.right,curr_sum,path)
            path.pop()
            #This Step is Important while passing a Mutable list as slate.
            # for #7 the if condition is not met
            # 7 ---> Two null nodes on Left and Right
            # pops 7 off the path

            # then for #2  (7 is no longer on the path)
            # path.pop()

    

        
        helper(root,curr_sum,path)
        return res

        