# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minDiff = float("inf")

        prevNode = None

        # Recursive O(n), O(n)

        # def helper(node):
        #     nonlocal minDiff, prevNode
            
            
        #     if node is None:
        #         return
        #     helper(node.left)
        #     if prevNode is not None:
        #         minDiff = min(minDiff, (node.val - prevNode.val))

        #     prevNode = node
        #     helper(node.right)

        # helper(root)
        # return minDiff

        # Iterative
        stack = []
        curr = root
        inorder = []

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            node = stack.pop()
            inorder.append(node.val)
            if prevNode is not None:
                minDiff = min(minDiff, (node.val - prevNode.val))
            prevNode = node
            
            curr = node
            curr = curr.right
        # print(inorder)
        return minDiff


            


         