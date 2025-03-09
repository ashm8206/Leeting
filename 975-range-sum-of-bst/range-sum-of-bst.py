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

        # Method II
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
        # https://leetcode.com/problems/search-in-a-binary-search-tree/description/


        # How to optimize for 10^9

#         class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class RangeSumCalculator:
#     def __init__(self, root):
#         self.vals = []
#         self.prefix_sums = []
#         self._inorder(root)
#         self.inorder = []
    
#     def _inorder(self, root):
#         """Perform inorder traversal to sort values and build prefix sums"""
#         if not root:
#             return
        
#         self._inorder(root.left)
        
#         self.vals.append(root.val)
#         # self.inorder.append(root.val)
        
#         if not self.prefix_sums:
#             self.prefix_sums.append(root.val)
#         else:
#             self.prefix_sums.append(self.prefix_sums[-1] + root.val)
            
#         self._inorder(root.right)
    
#     def _find_right_boundary(self, left, right, upper):
#         """Find the rightmost index where vals[index] <= upper"""
#         while left <= right:
#             mid = left + (right - left) // 2
#             if self.vals[mid] <= upper:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return right
    
#     def _find_left_boundary(self, left, right, lower):
#         """Find the leftmost index where vals[index] >= lower"""
#         while left <= right:
#             mid = left + (right - left) // 2
#             if self.vals[mid] >= lower:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         return left
    
#     def calculate(self, lower, upper):
#         print(self.prefix_sums)
#         print(self.vals)
        
#         # print(self.inorder)
#         """Calculate the sum of values in range [lower, upper]"""

          # exact Binary search
#         right_boundary = self._find_right_boundary(0, len(self.vals) - 1, upper)
#         left_boundary = self._find_left_boundary(0, len(self.vals) - 1, lower)
        
#         print(left_boundary, right_boundary)
#         print(lower, upper)
#         print("----")
        
#         if left_boundary == 0:
#             return self.prefix_sums[right_boundary]
#         return self.prefix_sums[right_boundary] - self.prefix_sums[left_boundary - 1]

# # Example usage and test cases
# def test_range_sum_calculator():
#     # Build the tree
#     root = TreeNode(10)
#     root.left = TreeNode(5)
#     root.left.left = TreeNode(3)
#     root.left.left.left = TreeNode(1)
#     root.left.right = TreeNode(7)
#     root.left.right.left = TreeNode(6)
#     root.right = TreeNode(15)
#     root.right.right = TreeNode(15)
#     root.right.left = TreeNode(13)
#     root.right.right.right = TreeNode(18)
    
#     # Create the calculator
#     calculator = RangeSumCalculator(root)
    
#     # Test cases
#     assert calculator.calculate(5, 16) == 56+15
#     assert calculator.calculate(0, 9000) == 1+3+5+6+7+10+13+15+15+18
#     assert calculator.calculate(7, 7) == 7
#     assert calculator.calculate(8, 9) == 0
#     assert calculator.calculate(14, 18) == 33
#     assert calculator.calculate(3, 6) == 14
    
#     print("All tests passed!")

# if __name__ == "__main__":
#     test_range_sum_calculator()
        