# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse(self, head, k):
        # 1, 2, 3, 4

        if head is None or head.next is None:
            return head

        prev = None
        curr = head
        while k:
            new_node = curr.next
            curr.next = prev
            prev = curr
            curr = new_node
            k-=1
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
            curr = head
            count = 0

            while curr and count < k:
                count+=1
                curr = curr.next 
              
            if count==k:
                prev = self.reverse(head,k)
                head.next = self.reverseKGroup(curr, k)
                return prev
            else: # leave as is # Nodes < K
                return head
            

            #  Reverse Nodes Irrespective of How many Remain?

            # if head is None or head.next is None:
            #     return head

            # prev = None
            # curr = head
            # count = 0
            # while curr and count < k:
            #     new_node = curr.next
            #     curr.next = prev
            #     prev = curr
            #     curr = new_node
            #     count+=1
            # if curr:
            #     # if curr.beyond k
            #     head.next = self.reverseKGroup(curr,k)

            #     # 1, 2, 3,  4, 5, 6
            #     # head  prev     RH
            #     # 3, 2, 1 --> 6, 5, 4

            # return prev # Reverse LinkedList
       




