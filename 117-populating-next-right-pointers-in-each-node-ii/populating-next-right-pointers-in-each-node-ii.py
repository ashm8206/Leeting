"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        #Method I Queue
        # if not root:
        #     return root
        
        # q = collections.deque()
        # q.append(root)

        # while q:
        #     lenQ = len(q)
        
        #     for i in range(lenQ):
        #         node = q.popleft()

        #         if i < lenQ-1:
        #             node.next = q[0]
                
        #         if node.left:
        #             q.append(node.left)
                
        #         if node.right:
        #             q.append(node.right)
        # return root
                
        # Level2curr.next = if L1right then L1Right else : # Level1curr = Level1.next 
        # Level2curr= Level2.next

        # Method 2 
        # Pointers, Space O(1)
        
        def process(childNode, prev, leftmost):
            if childNode:
                if prev is None:
                    leftmost = childNode
                else:
                    prev.next = childNode

                prev = childNode

            return prev, leftmost

        if not root:
            return root
        
        leftmost = root

        while leftmost: 

            # leftmost  Always comes from previous level.
            # for Leaf Node, leftmost never gets set 
            #  so after curr --> reach None

            #  we break out of Outer leftmost Node too
        

            curr = leftmost
            # Now Leftmost becomes Head of Parent List

            # before every level, prev is None, and leftmost is None
            prev = None 
            leftmost = None
            while curr:

                prev, leftmost = process(curr.left, prev, leftmost)
                
                # if leftmost:
                #     print(curr.val, leftmost.val)
                # else:
                #     print(curr.val, None)
                prev, leftmost = process(curr.right, prev, leftmost)
                # left most can be right child'd leftmost
                #  So it is Required!
                
            
                curr = curr.next
                # move through the parent level with next pointer
                # parent level is already linked

        return root
        


                
        

        