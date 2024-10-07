# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
        if head is None or head.next is None:
            return head
        # Iterative
        # prev, curr = None, head 

        # # dummy = ListNode(-1)
        # # dummy.next = head

        # curr = head
        # prev = None

        # while curr:

        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp

        # # dummy.next = prev

        # # return dummy.next 
        # return prev


        #Recursion Method I # Give New head

        # TakeYouForward https://www.youtube.com/watch?v=D2vI2DNJGd8&t=920s
        newHead = self.reverseList(head.next)
        last = head.next
        last.next = head
        head.next = None

        return newHead

        # newHead = None
        # Method II - Give the last value 
        # def helper(head):
        #     nonlocal newHead
        #     if head is None or head.next is None:
        #         if newHead is None:
        #             newHead = head
        #         return head
            
        #     last = helper(head.next)
        #     last.next = head
        #     head.next = None
        #     last = head

        #     return last

        # helper(head)
        # return newHead


        
