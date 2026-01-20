# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
    # Total 21
    # 1; 10,  11. = 110
    # 2: 12   9.  = 108
    # 3, 17, 4.   =  68
    # 4. 16  5.   = 80
    # 5. 15, 6.   = 90

    # 1: Prefix Sum and Store in R 
    # 2. total Count =  counts
    # 3. Need visited array

    # 4: One more VLR
        maxProd = 0
        MOD = 10**9 + 7
        allSum = []
        def get_tree_sum(root):
            if root is None:
                return 0
            left_sum = get_tree_sum(root.left)
            right_sum = get_tree_sum(root.right)
            total_substree_sum = root.val + left_sum + right_sum
            allSum.append(total_substree_sum)
            return total_substree_sum
        
        total_sum =  get_tree_sum(root)

        for subtree_sum in allSum:
            maxProd = max(maxProd, (total_sum - subtree_sum) * subtree_sum)
        
        return maxProd % MOD

        # def helper(root):
        #     nonlocal maxProd, total_sum

        #     if root is None:
        #         return 0
            
        #     leftSum = helper(root.left)
        #     rightSum = helper(root.right)

        #     total_sub_tree_sum = (root.val + leftSum + rightSum)
        #     product = (total_sub_tree_sum * (total_sum - total_sub_tree_sum))

        #     maxProd = max(product, maxProd)

        #     return total_sub_tree_sum

        # helper(root)
        # return maxProd % MOD