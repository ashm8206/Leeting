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
        
        # slow, fast = head, head
        # # if odd len then middle node remain attached to first half
        # while fast.next and fast.next.next:
    
        #     # Mid pt to comapre
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow
        

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find Middle
        # Reverse second half in place
        # start comparing

        if head is None or head.next is None:
            return True

        mid = self.findMiddle(head)
        l2 = self.reverse(mid)
        l1 = head


    
        # l1, l2 = head, self.reverse(mid.next) # reversed second lst
        

        while l2 is not None:
        
            if l1.val!=l2.val:
                return False

            l1=l1.next
            l2=l2.next

        # mid.next = self.reverse(mid.next)
        return True

        