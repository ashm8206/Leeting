from collections import OrderedDict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        # List to store the boundary values
        boundary_values = []
      
        # Return empty list if the tree is empty
        if not root:
            return boundary_values
      
        # Include the root value if it is not a leaf node
        if not self.isLeaf(root):
            boundary_values.append(root.val)

        # Process left boundary (excluding leaves and root)
        temp = root.left
        while temp:
            if not self.isLeaf(temp):
                boundary_values.append(temp.val)
            temp = temp.left if temp.left else temp.right

        # Process all leaves
        self.addLeaves(root, boundary_values)

        # Process right boundary (excluding leaves and root) in reverse order
        stack = []
        temp = root.right
        while temp:
            if not self.isLeaf(temp):
                stack.append(temp.val)
            temp = temp.right if temp.right else temp.left
      
        # Add the right boundary values to the result in the correct order
        while stack:
            boundary_values.append(stack.pop())

        # Return the complete boundary of the binary tree
        return boundary_values

    def addLeaves(self, node: TreeNode, boundary_values: List[int]):
        # Base case: if it is a leaf node, add to the list
        if self.isLeaf(node):
            boundary_values.append(node.val)
      
        # Recursively add left and right leaves
        if node.left:
            self.addLeaves(node.left, boundary_values)
        if node.right:
            self.addLeaves(node.right, boundary_values)

    def isLeaf(self, node: TreeNode) -> bool:
        # Check if the node is a leaf node
        return node is not None and node.left is None and node.right is None


        # def leftBoundary(root):
        #     if not root:
        #         return 

        #     if root.left or root.right:
        #         res.append(root.val)

        #     curr = root.left
        #     while curr:
        #         if curr.left or curr.right:
        #             res.append(curr.val)
        #             print(res)
        #         if curr.left:
        #             curr = curr.left
        #         else:
        #             curr = curr.right
        #     # print('Left Finish')
        
        # def addLeaves(root):
        #     if not root:
        #         return
        #     if root.left is None and root.right is None:
        #         res.append(root.val)
        #     addLeaves(root.left)
        #     addLeaves(root.right)

        # def rightBoundary(root):
        #     stack = []
        #     curr = root.right
        
        #     while curr:
        #         if curr.left or curr.right:
        #             stack.append(curr.val)
        #         if curr.right:
        #             curr = curr.right
        #         else:
        #             curr = curr.left
        #     return stack

        # leftBoundary(root)
        # addLeaves(root)
        # stack = rightBoundary(root)

        # while stack:
        #     reversed_val = stack.pop()
        #     res.append(reversed_val)

        # # print(res)
        # return res