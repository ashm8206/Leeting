"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':

        if head is None :
            head = Node(insertVal)
            head.next = head
            return head

    
        curr = head

        while curr.next!=head:
            if  curr.val <= curr.next.val:
                if curr.val <= insertVal and insertVal<=curr.next.val:
                    break
            else:
                if curr.val <= insertVal or insertVal<=curr.next.val:
                    break

            curr = curr.next

        # newNodenext = curr.next
        # curr.next = Node(insertVal, newNodenext)
        ''' OR '''
        newNodeNext = curr.next
        newNode = Node(insertVal)
        curr.next = newNode
        newNode.next = newNodeNext

        return head
        
