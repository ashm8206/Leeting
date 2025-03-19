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
        def helper(root):
            nonlocal diameter

            if root is None:
                return 0
            res = [0] # all child diameter, add 0 to catch empty child
            for child in root.children:
                res.append(helper(child))
            
            res.sort()
            max_child = res[-1]
            if len(res) >=2:
                second_max = res[-2]
                diameter = max(diameter, max_child + second_max)

            return 1 + max_child #(use the max path)

        helper(root)

        return diameter


            
