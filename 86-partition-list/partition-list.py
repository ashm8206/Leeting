# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        #  Space: O(1)
        # You are taking the existing linked list and adjusting pointers 
        # + creating two dummy nodes. 
        # The additional memory is constant regardless of input size.

        if head is None or head.next is None:
            return head
        
        beforeHead = ListNode(-101)
        afterHead = ListNode(-101)

        #runners
        before = beforeHead
        after = afterHead
        curr = head
    
        while curr:
            temp = curr.next
            curr.next = None

            if curr.val < x:
                before.next = curr
                before = before.next 
                # while curr then:...
                #           ensures that before is not None
            else:
                after.next = curr
                after = after.next
            curr = temp
        
        before.next = afterHead.next
        return beforeHead.next
        
        