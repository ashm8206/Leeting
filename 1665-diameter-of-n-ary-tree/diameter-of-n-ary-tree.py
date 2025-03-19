"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        diameter = 0

        def get_top_2_max(nums):
            first_max= float(-inf)
            second_max = float(-inf)

            for num in nums:
                if num >= first_max:
                    second_max = first_max
                    first_max = num
                elif num > second_max and num <= first_max:
                    second_max = num
            return first_max, second_max

        def helper(root):
            nonlocal diameter

            if root is None:
                return 0
            res = [0,0] # all child diameter, add 0 to catch empty child
            for child in root.children: 
                res.append(helper(child))
            
            max_child, second_max = get_top_2_max(res)

            # if second_max!=float("-inf"):
            diameter = max(diameter, max_child + second_max)

            return 1 + max_child #(use the max path)

        helper(root)
        return diameter

        


            
