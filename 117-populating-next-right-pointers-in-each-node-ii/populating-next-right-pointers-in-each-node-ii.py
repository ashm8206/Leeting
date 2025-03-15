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
        
        # white board will help
        if not root:
            return None

        head = root # changes each level
        dummy = Node(-1) # ptrs to next level

        while head:
            curr = head
            post = dummy
            while curr:
                if curr.left:
                    post.next = curr.left
                    post = post.next
                if curr.right:
                    post.next = curr.right
                    post = post.next

                curr = curr.next 
                # curr level already linked, move to the next one
            head = dummy.next
            
            dummy.next = None #Unlink to re-purpose this dummy node.
        return root
        
      