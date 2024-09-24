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
                # 3,|-4-| 5,  1. First casee
                if curr.val <= insertVal and insertVal<=curr.next.val:
                    break
            else:
                # curr.val > curr.next.val

                # 3, 5,  6| 0 1. First casee

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
        
