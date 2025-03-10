# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        odd = head
        even = head.next
        evenHead = even
        # better to use even:
        # will ensure odd.next [ will always be present]

        # odd and odd.next :  
        # with odd.next outside loop, is problem
        # odd can becomes None : Even Inputs!
        while even and even.next:

            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next
        
        odd.next = evenHead
        return head


