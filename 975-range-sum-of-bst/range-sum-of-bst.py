# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Method I
        # queue = collections.deque()

        # queue.append(root)

        # res = 0

        # # I want to touch each node once
        # while queue:
        #     node = queue.popleft()
        #     if low <= node.val <= high:
        #         res+=node.val
            
        #     if node.left:
        #         queue.append(node.left)
            
        #     if node.right:
        #         queue.append(node.right)

        # return res

        def dfs(root):
            nonlocal ans
            if not root:
                return 
            if low <= root.val <= high:
                    ans += root.val
            if low < root.val:
                dfs(root.left)
            if root.val < high:
                dfs(root.right)
        ans = 0
        dfs(root)
        return ans

        #  Method II

        # def dfs(node):
        #     nonlocal ans
        #     if node:
        #         if low <= node.val <= high:
        #             ans += node.val
        #         if low < node.val:
        #             dfs(node.left)
        #         if node.val < high:
        #             dfs(node.right)

        # ans = 0
        # dfs(root)
        # return ans
