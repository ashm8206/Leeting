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
            if curr.val <= node.val <= curr.next.val:
                break
            # case: 3 -> 1
            if curr.val > curr.next.val and (node.val > curr.val or node.val < curr.next.val):
                break
            
            curr = curr.next

        # insert node
        node.next = curr.next
        curr.next = node

        return head