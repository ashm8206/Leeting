# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # if (head is None or head.next is None) and n == 1:
        #     return None
        dummy = ListNode(-1)
        dummy.next = head

        slow = dummy
        fast = dummy

        # -1 , 1, 2,  3
        #         s   f

        #-1, 1
        # 2. 1 (f)
        # s.next -> Null
        # dummy.next

    
        i = n
        while i:
            fast = fast.next
            i -= 1

        while fast.next:
            fast = fast.next
            slow = slow.next
            
            
        slow.next = slow.next.next
        return dummy.next

       