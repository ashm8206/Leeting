# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        
        n = 1
        old_tail = head
        while old_tail.next:
            old_tail = old_tail.next
            n+=1

        if k%n==0:
            return head

        old_tail.next = head

        
        # Link the LinkedList and get Length of linkedlist in N

        # Old LK: # 1 > 2 > 3 > 4 > 5.  #k =2. # n = 5
        #  indx:    0   1   2   3   4
        # New LK: # 4 > 5 > 1 > 2 > 3 

        # New Tail (N-K -1)
        # New Head (N-K)

        new_tail = head
        for _ in range((n-k)%n - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next 
        new_tail.next = None
        # ^ Break the linkedList

        return new_head




