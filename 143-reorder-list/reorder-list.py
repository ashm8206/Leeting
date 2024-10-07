# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def middle(self, head) -> ListNode:
        slow, fast = head, head
        prev = None

        while fast and fast.next:
            # prev = slow 
            slow = slow.next
            fast = fast.next.next
        # if prev:
        #     prev.next = None
        return slow

    def reverse(self, head) -> ListNode:
        if head is None or head.next is None:
            return head
        
        newHead = self.reverse(head.next)
        last = head.next
        last.next = head
        head.next = None
        
        return newHead
        
        #Iterative

        # dummy = ListNode(-1)
        # dummy.next = head
        # prev = dummy
        # curr = head

        # while curr:
        #    new = curr.next
        #    curr.next = prev
        #    prev = curr
        #    curr = new 

        # dummy.next = prev
        # return dummy.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # middle of linkedlist
        # n/2 + 1 --> used in this prb
        # n/2-1
        prehead = ListNode(-1)
        prehead.next = head
        prev = prehead
        mid = self.middle(head)
        l1, l2 = head, self.reverse(mid)
      
        flip = 1
        while l1 is not None and l2 is not None:
            # print(l1.val, l2.val)
            if flip:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            flip^=1
            # print(l1.val if l1 else None, l2.val if l2 else None)
            # print("***")
            prev = prev.next
        # first half is still connected to second half at Mid
        # second half Mid is the last node and it is None

        # mid can be printed either by l1 or l2 branch
        # but as soon as it is printed, its Next is NONE
        #  AND we break out of l1 is Not None and l2 is Not None.
        
        # print(l1, l2)
        return prehead.next
       

    

