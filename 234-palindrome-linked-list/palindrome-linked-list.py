# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head:Optional[ListNode]) -> [ListNode]:

        prev = None
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

        
        # if head is None or head.next is None:
        #     return head
        
        # newHead = self.reverse(head.next)
        # front = head.next
        # front.next = head
        # head.next = None
        # return newHead

    def findMiddle(self, head:Optional[ListNode]) -> [ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find Middle, 
        #  Middle attached to L2 and L1
        #     Makes both L1 and L2 of equal len for Both odd and even Total lens

        # Reverse second half in place
        # start comparing with the L1

        if head is None or head.next is None:
            return True

        mid = self.findMiddle(head)

        l1 = head
        l2 = self.reverse(mid)
        

        while l2: 
            # same as while l1 and l2:  --> len(l1) == len(l2)
            # remeber findmiddle, 
            # keeps middle attached to l1  and reverses (l2 including middle)
            if l1.val!=l2.val:
                return False
            l1=l1.next
            l2=l2.next
        return True

        