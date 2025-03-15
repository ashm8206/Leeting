"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':

        node = Node(insertVal)
        if head is None :
            head = node
            head.next = head
            return head

    
        curr = head

        while curr.next!=head:
            # Case1: 1 <- Node(2) <- 3
            if curr.val <= node.val <= curr.next.val: # and 
                break
            # case: 3 -> 1 = Link Position
            #  3 > 1 and 3 -> 4 -> 1 or  3 -> 0 --> 1
            #  curr > curr.next.val
            if curr.val > curr.next.val and (curr.val <= node.val or node.val <= curr.next.val):
                break
            
            curr = curr.next

        # insert node
        node.next = curr.next
        curr.next = node

        return head