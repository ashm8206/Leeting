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
        
        if not root:
            return None
        
        
        dummy = Node(-1)
        head = root

        while head:
            curr  = head
            prev = dummy #dummy = -1

            while curr:
                if curr.left:
                    prev.next = curr.left
                    prev = prev.next
                if curr.right:
                    prev.next = curr.right
                    prev = prev.next

                curr = curr.next
            head = dummy.next
            # dummy.next =  pts to start of next level
            # at each level prev.next 
            #      = first present node in next level
            dummy.next = None
            #unlink this
        return root
        


                
        

        