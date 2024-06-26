# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
#         res = []

#         def helper(node,path):

#             path+=str(node.val)

#             if node.left is None and node.right is None:
#                 res.append((path))
#                 return
            
#             path+='->'

#             if node.left:
#                 helper(node.left, path)
        
#             if node.right:
#                 helper(node.right, path)

#             # path.pop() # remove Left
#             # path.pop() # remove Right
        
#         helper(root,'')
#         return res

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def helper(node,path):

            if not node:
                return

            if node.left is None and node.right is None:
                path.append(str(node.val))
                res.append("->".join(path[:]))
                # it was popping the 5, when it should have popped 2
                # we added addiional pop here to pop the left node
                
                return
            
            # path+='->'
            path.append(str(node.val))
            if node.left:
                helper(node.left, path)
                path.pop()

            if node.right:
                helper(node.right, path)
                path.pop()

            
        
        helper(root,[])
        return res

# class Solution:
#   def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
#     ans = []

#     def dfs(root: Optional[TreeNode], path: List[str]) -> None:
#       if not root:
#         return
#       if not root.left and not root.right:
#         ans.append(''.join(path)  +str(root.val))
#         return

#       path.append(str(root.val)+'->')
#       if root.left:
#         dfs(root.left, path)
#       if root.right:
#         dfs(root.right, path)
#       path.pop()

#     dfs(root, [])
#     return ans