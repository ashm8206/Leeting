"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
        
        curr = head

        # A-->A'-->B-->B'
        while curr:
            new_node = Node(curr.val, None, None)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next
        
        # Set Random ptrs

        curr = head
        while curr and curr.next:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        ptrA = head
        ptrB = head.next
        newHead = head.next
        # dummy = Node(-1)
        # dummy.next = head.next

        while ptrA.next and ptrB.next:
            ptrA.next = ptrB.next
            ptrA = ptrA.next

            ptrB.next = ptrA.next
            ptrB = ptrB.next
           
        return newHead


    
    


