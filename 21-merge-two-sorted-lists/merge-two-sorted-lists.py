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

        curr = new_head = ListNode(0)
        l1 = list1
        l2 = list2
        while l1 or l2:
            if l2 is None or (l1 and l1.val < l2.val):
                curr.next, l1 = l1, l1.next
            else:
                curr.next, l2 = l2, l2.next
            curr = curr.next
        return new_head.next