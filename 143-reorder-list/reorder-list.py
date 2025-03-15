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
            # we check fast.next to ensure we can take 2 steps
            # 1x : 2x fast
            # 1x --> reach the middle most point
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return slow

    def reverse(self, head) -> ListNode:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head

        # this will put middle in l2
        # remember to detach the prev from Middle

        mid = self.middle(head)

        l1, l2 = head, self.reverse(mid)

    
        prehead = ListNode(-1)
        prehead.next = head
        curr = prehead
        while l1 or l2:
            if l1:
                curr.next, l1 = l1, l1.next
                curr = curr.next
            if l2: # one and then the other. # no else
                curr.next, l2 = l2, l2.next
                curr = curr.next

        return prehead.next
        