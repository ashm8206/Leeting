# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getMid(self, head):
        slow = head
        fast = head
        midPrev = None
        while fast and fast.next:
            midPrev = slow
            slow = slow.next
            fast = fast.next.next
        midPrev.next = None
        return slow
    
    def merge(self, left, right):

        preHead = ListNode(-1)
        prev = preHead

        while left or right:
            if left is None:
                prev.next = right 
                right = None
            elif right is None:
                prev.next = left 
                left = None
            elif left.val <= right.val:
                prev.next = left
                left = left.next
            else:
                prev.next = right
                right = right.next
            prev = prev.next

        return preHead.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left,right)

