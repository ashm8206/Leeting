"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        # https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/solutions/932499/simple-python-solution-with-o-1-space-complexity/

        # if either points to root, we set it to other nodes, starting point

        pA = p
        pB = q
        # Make a cycle
        while pA != pB:
            pA = q if pA is None else pA.parent
            pB = p if pB is None else pB.parent

        return pA

        
        
"""
P: p1 -> p2 -> p3 -> c1 -> c2 -> c3
Q: q1 -> c1 -> c2 -> c3
The idea is that by concatenating the paths of P and Q, resulting in:
P -> Q: (p1 -> p2 -> p3 -> c1 -> c2 -> c3)-> (q1 -> c1 -> c2 -> c3)
Q -> P: (q1 -> c1 -> c2 -> c3) -> (p1 -> p2 -> p3 -> c1 -> c2 -> c3)
You can see the length of P -> Q is equal to Q -> P and they both end at c3.
Given the fact that there is a common path at the end of P -> Q and Q -> P which is c1 -> c2 -> c3, this guarantees that these two paths P -> Q and Q -> P with definitely reach a common node in somewhere, and the first encountered common node is the LCA.

For the special case where the LCA is q (or p):
P: p1 -> p2 -> q -> c1 -> c2 -> c3
Q: q -> c1 -> c2 -> c3
By concatenating the paths of P and Q, resulting in:
P -> Q: (p1 -> p2 -> q -> c1 -> c2 -> c3) ->(q -> c1 -> c2 -> c3)
Q -> P: (q -> c1 -> c2 -> c3) -> (p1 -> p2 -> q -> c1 -> c2 -> c3)
"""


        #https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/solutions/933885/java-100-this-is-a-linked-list-question/
        #https://leetcode.com/problems/intersection-of-two-linked-lists/description/
