from collections import OrderedDict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        boundary_values = []

        if not self.isLeaf(root):
            boundary_values.append(root.val)
        
        temp = root.left
        while temp:
            if not self.isLeaf(temp):
                boundary_values.append(temp.val)
            if temp.left:
                temp = temp.left
            else:
                temp = temp.right
        
        # addLeaves
        self.addLeaves(root, boundary_values)

        right_values = [] # needs to be reversed
        temp = root.right
        while temp:
            if not self.isLeaf(temp):
                right_values.append(temp.val)
            if temp.right:
                temp = temp.right
            else:
                temp = temp.left
                
        while right_values:
            boundary_values.append(right_values.pop())
        
        return boundary_values


    def addLeaves(self, root, boundary_values):
        if not root:
            return 
        
        if root.left is None and root.right is None:
            boundary_values.append(root.val)

        self.addLeaves(root.left,boundary_values )
        self.addLeaves(root.right,boundary_values )


    
    def isLeaf(self, node):
        if node:
            return node.left is None and node.right is None
        




    #     # List to store the boundary values
    #     boundary_values = []
      
    #     # Return empty list if the tree is empty
    #     if not root:
    #         return boundary_values
      
    #     # Include the root value if it is not a leaf node
    #     if not self.isLeaf(root):
    #         boundary_values.append(root.val)

    #     # Process left boundary (excluding leaves and root)
    #     temp = root.left
    #     while temp:
    #         if not self.isLeaf(temp):
    #             boundary_values.append(temp.val)
    #         temp = temp.left if temp.left else temp.right

    #     # Process all leaves
    #     self.addLeaves(root, boundary_values)

    #     # Process right boundary (excluding leaves and root) in reverse order
    #     stack = []
    #     temp = root.right
    #     while temp:
    #         if not self.isLeaf(temp):
    #             stack.append(temp.val)
    #         temp = temp.right if temp.right else temp.left
      
    #     # Add the right boundary values to the result in the correct order
    #     while stack:
    #         boundary_values.append(stack.pop())

    #     # Return the complete boundary of the binary tree
    #     return boundary_values

    # def addLeaves(self, node: TreeNode, boundary_values: List[int]):
    #     # Base case: if it is a leaf node, add to the list
    #     if self.isLeaf(node):
    #         boundary_values.append(node.val)
      
    #     # Recursively add left and right leaves
    #     if node.left:
    #         self.addLeaves(node.left, boundary_values)
    #     if node.right:
    #         self.addLeaves(node.right, boundary_values)

    # def isLeaf(self, node: TreeNode) -> bool:
    #     # Check if the node is a leaf node
    #     return node is not None and node.left is None and node.right is None
