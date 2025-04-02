"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #res = []
      

        def get_last(node):
            t = node
            while t.next:
                t = t.next
            return t
        
        curr = head
        while curr:
            if curr.child:
                curr_next = curr.next
                curr.next = curr.child
                curr.child.prev = curr
                last_child = get_last(curr.child)
                if curr_next:
                    curr_next.prev = last_child
                    
                last_child.next = curr_next
                curr.child = None
            curr = curr.next
        
        return head

