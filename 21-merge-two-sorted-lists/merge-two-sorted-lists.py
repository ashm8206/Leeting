# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Recursive
        # if list1 is None:
        #     return list2
        # elif list2 is None:
        #     return list1
        # elif list1.val <= list2.val:
        #     list1.next = self.mergeTwoLists(list1.next, list2)
        #     return list1
        # else:
        #     list2.next = self.mergeTwoLists(list1, list2.next)
        #     return list2

        # Iterative
        p1 = list1
        p2 = list2
        prehead = ListNode(-1)

        prev = prehead

        while p1 or p2:

            if p1 is None:
                prev.next = p2
                p2 = None
            
            elif p2 is None:
                prev.next = p1
                p1 = None

            elif p1.val <= p2.val:
                prev.next = p1
                p1 = p1.next
            else:
                prev.next = p2
                p2 = p2.next
                
            prev = prev.next

       

        return prehead.next